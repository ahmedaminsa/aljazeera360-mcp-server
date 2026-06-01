FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py .

# Expose port for HTTP/SSE transport
EXPOSE 8080

# Default to HTTP transport for cloud deployment
ENV MCP_TRANSPORT=sse
ENV MCP_PORT=8080

CMD ["python", "server.py"]
