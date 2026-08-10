import { defineTool } from "@lovable.dev/mcp-js";
import { services } from "../content";

export default defineTool({
  name: "list_services",
  title: "List SALocations services",
  description:
    "List the core services SALocations offers — destination experience design, luxury concierge, production support, content creation, adventure experiences, destination marketing and digital nomad concierge.",
  inputSchema: {},
  annotations: { readOnlyHint: true, idempotentHint: true, openWorldHint: false },
  handler: () => ({
    content: [{ type: "text" as const, text: JSON.stringify(services, null, 2) }],
    structuredContent: { services },
  }),
});
