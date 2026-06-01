"""
Al Jazeera 360 MCP Server — Analytics & Request Tracking
=========================================================
Tracks every tool call made to the MCP server:
- Which tool was called
- When it was called
- What parameters were used
- Which AI client made the request (User-Agent)
- How long it took
- Whether it succeeded or failed

Data is stored in a local SQLite database for zero-config setup.
Provides a simple HTTP dashboard and JSON API for viewing stats.
"""

import json
import os
import sqlite3
import time
import threading
from datetime import datetime, timedelta
from typing import Optional
from functools import wraps
from http.server import HTTPServer, BaseHTTPRequestHandler

# ============================================================================
# Configuration
# ============================================================================

DB_PATH = os.environ.get("AJ360_ANALYTICS_DB", "analytics.db")
DASHBOARD_PORT = int(os.environ.get("AJ360_DASHBOARD_PORT", "9090"))
ENABLE_DASHBOARD = os.environ.get("AJ360_ENABLE_DASHBOARD", "true").lower() == "true"

# ============================================================================
# Database Setup
# ============================================================================

_db_lock = threading.Lock()


def _get_db():
    """Get a thread-local database connection."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the analytics database."""
    conn = _get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            tool_name TEXT NOT NULL,
            parameters TEXT,
            client_info TEXT,
            duration_ms REAL,
            success INTEGER DEFAULT 1,
            error_message TEXT,
            result_count INTEGER DEFAULT 0
        );
        
        CREATE INDEX IF NOT EXISTS idx_requests_timestamp ON requests(timestamp);
        CREATE INDEX IF NOT EXISTS idx_requests_tool ON requests(tool_name);
        CREATE INDEX IF NOT EXISTS idx_requests_client ON requests(client_info);
    """)
    conn.commit()
    conn.close()


# ============================================================================
# Request Tracker
# ============================================================================

class RequestTracker:
    """Tracks and records all MCP tool calls."""
    
    def __init__(self):
        init_db()
    
    def record(
        self,
        tool_name: str,
        parameters: dict = None,
        client_info: str = None,
        duration_ms: float = 0,
        success: bool = True,
        error_message: str = None,
        result_count: int = 0,
    ):
        """Record a tool call to the database."""
        with _db_lock:
            conn = _get_db()
            conn.execute(
                """INSERT INTO requests 
                   (timestamp, tool_name, parameters, client_info, duration_ms, success, error_message, result_count)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    datetime.utcnow().isoformat(),
                    tool_name,
                    json.dumps(parameters or {}, ensure_ascii=False),
                    client_info or "unknown",
                    duration_ms,
                    1 if success else 0,
                    error_message,
                    result_count,
                ),
            )
            conn.commit()
            conn.close()
    
    def get_stats(self, days: int = 7) -> dict:
        """Get analytics summary for the last N days."""
        since = (datetime.utcnow() - timedelta(days=days)).isoformat()
        conn = _get_db()
        
        # Total requests
        total = conn.execute(
            "SELECT COUNT(*) as count FROM requests WHERE timestamp >= ?", (since,)
        ).fetchone()["count"]
        
        # Success rate
        successful = conn.execute(
            "SELECT COUNT(*) as count FROM requests WHERE timestamp >= ? AND success = 1", (since,)
        ).fetchone()["count"]
        
        # Requests per tool
        tools = conn.execute(
            """SELECT tool_name, COUNT(*) as count, AVG(duration_ms) as avg_duration
               FROM requests WHERE timestamp >= ?
               GROUP BY tool_name ORDER BY count DESC""",
            (since,),
        ).fetchall()
        
        # Requests per client
        clients = conn.execute(
            """SELECT client_info, COUNT(*) as count
               FROM requests WHERE timestamp >= ?
               GROUP BY client_info ORDER BY count DESC""",
            (since,),
        ).fetchall()
        
        # Top searches
        searches = conn.execute(
            """SELECT parameters, COUNT(*) as count
               FROM requests WHERE timestamp >= ? AND tool_name = 'search_videos'
               GROUP BY parameters ORDER BY count DESC LIMIT 20""",
            (since,),
        ).fetchall()
        
        # Daily breakdown
        daily = conn.execute(
            """SELECT DATE(timestamp) as day, COUNT(*) as count
               FROM requests WHERE timestamp >= ?
               GROUP BY DATE(timestamp) ORDER BY day DESC""",
            (since,),
        ).fetchall()
        
        # Hourly distribution (last 24h)
        last_24h = (datetime.utcnow() - timedelta(hours=24)).isoformat()
        hourly = conn.execute(
            """SELECT strftime('%H', timestamp) as hour, COUNT(*) as count
               FROM requests WHERE timestamp >= ?
               GROUP BY strftime('%H', timestamp) ORDER BY hour""",
            (last_24h,),
        ).fetchall()
        
        # Most requested content
        content_requests = conn.execute(
            """SELECT parameters, tool_name, COUNT(*) as count
               FROM requests WHERE timestamp >= ? 
               AND tool_name IN ('get_video_details', 'get_series_details', 'browse_section')
               GROUP BY parameters, tool_name ORDER BY count DESC LIMIT 20""",
            (since,),
        ).fetchall()
        
        conn.close()
        
        # Parse search terms
        top_searches = []
        for row in searches:
            try:
                params = json.loads(row["parameters"])
                term = params.get("query", params.get("topic", ""))
                if term:
                    top_searches.append({"term": term, "count": row["count"]})
            except (json.JSONDecodeError, TypeError):
                pass
        
        return {
            "period": f"Last {days} days",
            "since": since,
            "total_requests": total,
            "successful_requests": successful,
            "failed_requests": total - successful,
            "success_rate": f"{(successful / total * 100):.1f}%" if total > 0 else "N/A",
            "tools_usage": [
                {
                    "tool": row["tool_name"],
                    "calls": row["count"],
                    "avg_response_ms": round(row["avg_duration"], 1) if row["avg_duration"] else 0,
                }
                for row in tools
            ],
            "clients": [
                {"client": row["client_info"], "requests": row["count"]}
                for row in clients
            ],
            "top_searches": top_searches,
            "daily_breakdown": [
                {"date": row["day"], "requests": row["count"]}
                for row in daily
            ],
            "hourly_distribution": [
                {"hour": f"{row['hour']}:00", "requests": row["count"]}
                for row in hourly
            ],
            "most_requested_content": [
                {
                    "tool": row["tool_name"],
                    "parameters": row["parameters"],
                    "count": row["count"],
                }
                for row in content_requests
            ],
        }
    
    def get_recent_requests(self, limit: int = 50) -> list:
        """Get the most recent requests."""
        conn = _get_db()
        rows = conn.execute(
            """SELECT * FROM requests ORDER BY timestamp DESC LIMIT ?""",
            (limit,),
        ).fetchall()
        conn.close()
        
        return [
            {
                "id": row["id"],
                "timestamp": row["timestamp"],
                "tool": row["tool_name"],
                "parameters": row["parameters"],
                "client": row["client_info"],
                "duration_ms": row["duration_ms"],
                "success": bool(row["success"]),
                "error": row["error_message"],
                "result_count": row["result_count"],
            }
            for row in rows
        ]


# ============================================================================
# Analytics Decorator (wraps MCP tools)
# ============================================================================

# Global tracker instance
tracker = RequestTracker()


def track_request(tool_name: str):
    """Decorator to automatically track MCP tool calls."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            error_msg = None
            result_count = 0
            
            try:
                result = await func(*args, **kwargs)
                # Try to count results
                if isinstance(result, str):
                    try:
                        parsed = json.loads(result)
                        if isinstance(parsed, dict):
                            for key in ("items", "results", "episodes", "categories", "sections"):
                                if key in parsed:
                                    result_count = len(parsed[key])
                                    break
                    except (json.JSONDecodeError, TypeError):
                        pass
                return result
            except Exception as e:
                success = False
                error_msg = str(e)
                raise
            finally:
                duration_ms = (time.time() - start_time) * 1000
                tracker.record(
                    tool_name=tool_name,
                    parameters=kwargs if kwargs else ({"args": list(args)} if args else {}),
                    client_info=os.environ.get("MCP_CLIENT", "unknown"),
                    duration_ms=duration_ms,
                    success=success,
                    error_message=error_msg,
                    result_count=result_count,
                )
        return wrapper
    return decorator


# ============================================================================
# HTTP Dashboard
# ============================================================================

DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Al Jazeera 360 MCP — Analytics Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0a; color: #e0e0e0; padding: 24px; }
        h1 { font-size: 28px; margin-bottom: 8px; color: #fff; }
        h2 { font-size: 18px; margin: 24px 0 12px; color: #ccc; border-bottom: 1px solid #333; padding-bottom: 8px; }
        .subtitle { color: #888; font-size: 14px; margin-bottom: 32px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 32px; }
        .card { background: #1a1a1a; border: 1px solid #333; border-radius: 8px; padding: 20px; }
        .card .label { font-size: 12px; color: #888; text-transform: uppercase; letter-spacing: 1px; }
        .card .value { font-size: 32px; font-weight: 700; color: #fff; margin-top: 4px; }
        .card .value.green { color: #4ade80; }
        .card .value.blue { color: #60a5fa; }
        .card .value.yellow { color: #facc15; }
        table { width: 100%; border-collapse: collapse; background: #1a1a1a; border-radius: 8px; overflow: hidden; }
        th, td { padding: 10px 14px; text-align: left; border-bottom: 1px solid #222; font-size: 13px; }
        th { background: #222; color: #aaa; font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.5px; }
        td { color: #ddd; }
        .success { color: #4ade80; }
        .failure { color: #f87171; }
        .refresh-btn { background: #333; color: #fff; border: 1px solid #555; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-size: 13px; }
        .refresh-btn:hover { background: #444; }
        .bar { height: 6px; background: #60a5fa; border-radius: 3px; margin-top: 4px; }
        .section { margin-bottom: 32px; }
        .live-dot { display: inline-block; width: 8px; height: 8px; background: #4ade80; border-radius: 50%; margin-right: 6px; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
    </style>
</head>
<body>
    <h1><span class="live-dot"></span>Al Jazeera 360 MCP — Analytics</h1>
    <p class="subtitle">Real-time tracking of AI tool requests to your MCP server</p>
    
    <div id="dashboard">Loading...</div>
    
    <script>
        async function loadDashboard() {
            try {
                const [statsRes, recentRes] = await Promise.all([
                    fetch('/api/stats'),
                    fetch('/api/recent')
                ]);
                const stats = await statsRes.json();
                const recent = await recentRes.json();
                
                let html = '';
                
                // Summary cards
                html += '<div class="grid">';
                html += `<div class="card"><div class="label">Total Requests</div><div class="value blue">${stats.total_requests}</div></div>`;
                html += `<div class="card"><div class="label">Success Rate</div><div class="value green">${stats.success_rate}</div></div>`;
                html += `<div class="card"><div class="label">Failed</div><div class="value" style="color:#f87171">${stats.failed_requests}</div></div>`;
                html += `<div class="card"><div class="label">AI Clients</div><div class="value yellow">${stats.clients.length}</div></div>`;
                html += '</div>';
                
                // Tools usage
                html += '<div class="section"><h2>Tools Usage</h2><table><tr><th>Tool</th><th>Calls</th><th>Avg Response</th><th>Load</th></tr>';
                const maxCalls = Math.max(...stats.tools_usage.map(t => t.calls), 1);
                for (const tool of stats.tools_usage) {
                    const pct = (tool.calls / maxCalls * 100).toFixed(0);
                    html += `<tr><td><strong>${tool.tool}</strong></td><td>${tool.calls}</td><td>${tool.avg_response_ms}ms</td><td><div class="bar" style="width:${pct}%"></div></td></tr>`;
                }
                html += '</table></div>';
                
                // AI Clients
                if (stats.clients.length > 0) {
                    html += '<div class="section"><h2>AI Clients Making Requests</h2><table><tr><th>Client</th><th>Requests</th></tr>';
                    for (const c of stats.clients) {
                        html += `<tr><td>${c.client}</td><td>${c.requests}</td></tr>`;
                    }
                    html += '</table></div>';
                }
                
                // Top Searches
                if (stats.top_searches.length > 0) {
                    html += '<div class="section"><h2>Top Search Terms</h2><table><tr><th>Search Term</th><th>Count</th></tr>';
                    for (const s of stats.top_searches) {
                        html += `<tr><td>${s.term}</td><td>${s.count}</td></tr>`;
                    }
                    html += '</table></div>';
                }
                
                // Daily breakdown
                if (stats.daily_breakdown.length > 0) {
                    html += '<div class="section"><h2>Daily Activity</h2><table><tr><th>Date</th><th>Requests</th></tr>';
                    for (const d of stats.daily_breakdown) {
                        html += `<tr><td>${d.date}</td><td>${d.requests}</td></tr>`;
                    }
                    html += '</table></div>';
                }
                
                // Recent requests
                html += '<div class="section"><h2>Recent Requests (Live Feed)</h2><table><tr><th>Time</th><th>Tool</th><th>Client</th><th>Duration</th><th>Status</th></tr>';
                for (const r of recent.slice(0, 30)) {
                    const time = new Date(r.timestamp).toLocaleString();
                    const status = r.success ? '<span class="success">OK</span>' : `<span class="failure">${r.error || 'FAIL'}</span>`;
                    html += `<tr><td>${time}</td><td><strong>${r.tool}</strong></td><td>${r.client}</td><td>${r.duration_ms.toFixed(0)}ms</td><td>${status}</td></tr>`;
                }
                html += '</table></div>';
                
                html += '<p style="margin-top:24px;color:#666;font-size:12px;">Auto-refreshes every 10 seconds | <button class="refresh-btn" onclick="loadDashboard()">Refresh Now</button></p>';
                
                document.getElementById('dashboard').innerHTML = html;
            } catch (e) {
                document.getElementById('dashboard').innerHTML = '<p style="color:#f87171">Error loading dashboard: ' + e.message + '</p>';
            }
        }
        
        loadDashboard();
        setInterval(loadDashboard, 10000);
    </script>
</body>
</html>"""


class DashboardHandler(BaseHTTPRequestHandler):
    """HTTP handler for the analytics dashboard."""
    
    def log_message(self, format, *args):
        """Suppress default HTTP logs."""
        pass
    
    def do_GET(self):
        if self.path == "/" or self.path == "/dashboard":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(DASHBOARD_HTML.encode())
        
        elif self.path == "/api/stats":
            days = 7
            if "?" in self.path:
                try:
                    days = int(self.path.split("days=")[1])
                except (IndexError, ValueError):
                    pass
            stats = tracker.get_stats(days=days)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(stats, ensure_ascii=False).encode())
        
        elif self.path.startswith("/api/recent"):
            limit = 50
            if "?" in self.path:
                try:
                    limit = int(self.path.split("limit=")[1])
                except (IndexError, ValueError):
                    pass
            recent = tracker.get_recent_requests(limit=limit)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(recent, ensure_ascii=False).encode())
        
        elif self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        
        else:
            self.send_response(404)
            self.end_headers()


def start_dashboard(port: int = None):
    """Start the analytics dashboard HTTP server in a background thread."""
    port = port or DASHBOARD_PORT
    server = HTTPServer(("0.0.0.0", port), DashboardHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server
