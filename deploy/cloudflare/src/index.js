import { Container } from "@cloudflare/containers";

/**
 * Durable Object wrapping the Python MCP server container.
 *
 * All configuration the Python server needs is passed as environment
 * variables at container start. Secrets (AJ360_API_KEY, optionally
 * AJ360_REFRESH_TOKEN / AJ360_DASHBOARD_TOKEN) are Worker secrets
 * (`wrangler secret put ...`) forwarded into the container here.
 */
export class AJ360Container extends Container {
  defaultPort = 8080;
  // Keep the instance warm between MCP requests; it sleeps after idle
  // and cold-starts in a few seconds on the next request.
  sleepAfter = "15m";

  constructor(ctx, env) {
    super(ctx, env);
    this.envVars = {
      MCP_TRANSPORT: "streamable-http",
      MCP_PORT: "8080",
      // The standalone dashboard thread is pointless inside the container;
      // the dashboard routes are still served on the main port.
      AJ360_ENABLE_DASHBOARD: "false",
      AJ360_ALLOWED_HOST: env.AJ360_ALLOWED_HOST ?? "",
      AJ360_API_KEY: env.AJ360_API_KEY ?? "",
      AJ360_REFRESH_TOKEN: env.AJ360_REFRESH_TOKEN ?? "",
      AJ360_DASHBOARD_TOKEN: env.AJ360_DASHBOARD_TOKEN ?? "",
      AJ360_ENABLE_SEO_TOOLS: env.AJ360_ENABLE_SEO_TOOLS ?? "",
    };
  }
}

export default {
  async fetch(request, env) {
    // Single named instance: MCP streamable-http sessions must keep
    // hitting the same backend, and one container serves this fine.
    const container = env.AJ360_CONTAINER.getByName("mcp");
    return container.fetch(request);
  },
};
