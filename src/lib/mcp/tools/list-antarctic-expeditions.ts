import { defineTool } from "@lovable.dev/mcp-js";
import { antarcticExpeditions } from "../content";

export default defineTool({
  name: "list_antarctic_expeditions",
  title: "List Antarctic expeditions",
  description:
    "List SALocations' flagship Antarctic expeditions departing from Cape Town, including the emperor penguin expedition, South Pole private charter and wilderness camp.",
  inputSchema: {},
  annotations: { readOnlyHint: true, idempotentHint: true, openWorldHint: false },
  handler: () => ({
    content: [
      { type: "text" as const, text: JSON.stringify(antarcticExpeditions, null, 2) },
    ],
    structuredContent: { expeditions: antarcticExpeditions },
  }),
});
