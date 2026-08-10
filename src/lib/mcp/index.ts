import { defineMcp } from "@lovable.dev/mcp-js";
import listServices from "./tools/list-services";
import listSignatureExperiences from "./tools/list-signature-experiences";
import listAntarcticExpeditions from "./tools/list-antarctic-expeditions";
import getDigitalNomadConcierge from "./tools/get-digital-nomad-concierge";
import getContactDetails from "./tools/get-contact-details";

export default defineMcp({
  name: "sal-south-africa-elevated",
  title: "SAL: South Africa Elevated",
  version: "0.1.0",
  instructions:
    "Public tools for SALocations (SAL), a South African destination experience and marketing company. Use these tools to answer questions about SAL's services, signature South African experiences, Antarctic expeditions, the Digital Nomad Concierge Cape Town offering, and how to get in touch.",
  tools: [
    listServices,
    listSignatureExperiences,
    listAntarcticExpeditions,
    getDigitalNomadConcierge,
    getContactDetails,
  ],
});
