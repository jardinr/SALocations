import { defineTool } from "@lovable.dev/mcp-js";
import { contact, targetClients } from "../content";

export default defineTool({
  name: "get_contact_details",
  title: "Get SALocations contact details",
  description:
    "Get SALocations' public contact details, brand positioning and the types of clients it serves, for enquiries about booking an experience.",
  inputSchema: {},
  annotations: { readOnlyHint: true, idempotentHint: true, openWorldHint: false },
  handler: () => {
    const payload = { ...contact, targetClients };
    return {
      content: [{ type: "text" as const, text: JSON.stringify(payload, null, 2) }],
      structuredContent: payload,
    };
  },
});
