FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py .
COPY analytics.py .

# Expose ports: MCP server + Analytics dashboard
EXPOSE 8080 9090

# Default to Streamable HTTP transport for cloud deployment
ENV MCP_TRANSPORT=streamable-http
ENV MCP_PORT=8080
ENV AJ360_ENABLE_DASHBOARD=true
ENV AJ360_DASHBOARD_PORT=9090

CMD ["python", "server.py"]
