import { defineTool } from "@lovable.dev/mcp-js";
import { digitalNomadConcierge } from "../content";

export default defineTool({
  name: "get_digital_nomad_concierge",
  title: "Get Digital Nomad Concierge details",
  description:
    "Get details of the Digital Nomad Concierge Cape Town offering: what it covers, who it is for, and the page URL.",
  inputSchema: {},
  annotations: { readOnlyHint: true, idempotentHint: true, openWorldHint: false },
  handler: () => ({
    content: [
      { type: "text" as const, text: JSON.stringify(digitalNomadConcierge, null, 2) },
    ],
    structuredContent: digitalNomadConcierge,
  }),
});
