-- Usage analytics for the Al Jazeera 360 MCP server (Cloudflare D1).
--
-- Written by the Worker in front of the container, so it survives container
-- sleeps (unlike the in-container SQLite dashboard). Deliberately stores NO
-- IP addresses and no personal identifiers — only the AI client type, which
-- tool ran, the content query, and a coarse country code.

CREATE TABLE IF NOT EXISTS events (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  ts             TEXT NOT NULL,   -- ISO8601 UTC
  session_id     TEXT,            -- mcp-session-id (joins tool calls to their initialize row)
  method         TEXT,            -- initialize | tools/list | tools/call | ...
  tool           TEXT,            -- tool name when method = tools/call
  query          TEXT,            -- primary argument (search term, section, id), truncated
  client_name    TEXT,            -- from initialize params.clientInfo.name
  client_version TEXT,
  country        TEXT,            -- request.cf.country (coarse, no IP)
  ua             TEXT             -- truncated user-agent
);

CREATE INDEX IF NOT EXISTS idx_events_ts      ON events (ts);
CREATE INDEX IF NOT EXISTS idx_events_session ON events (session_id);
CREATE INDEX IF NOT EXISTS idx_events_tool    ON events (tool);
