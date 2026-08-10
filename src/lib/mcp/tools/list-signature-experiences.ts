import { defineTool } from "@lovable.dev/mcp-js";
import { signatureExperiences } from "../content";

export default defineTool({
  name: "list_signature_experiences",
  title: "List signature experiences",
  description:
    "List SALocations' signature South African experiences, such as the Luxury Cape Town Collection, Winelands escapes, safari journeys and remote star gazing, with their regions.",
  inputSchema: {},
  annotations: { readOnlyHint: true, idempotentHint: true, openWorldHint: false },
  handler: () => ({
    content: [
      { type: "text" as const, text: JSON.stringify(signatureExperiences, null, 2) },
    ],
    structuredContent: { experiences: signatureExperiences },
  }),
});
