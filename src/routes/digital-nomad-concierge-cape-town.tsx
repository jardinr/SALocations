import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import heroImg from "@/assets/dn-hero.jpg";
import accomImg from "@/assets/dn-accom.jpg";
import coworkingImg from "@/assets/dn-coworking.jpg";
import lifestyleImg from "@/assets/dn-lifestyle.jpg";
import { WhatsAppFloat } from "@/components/WhatsAppFloat";

export const Route = createFileRoute("/digital-nomad-concierge-cape-town")({
  head: () => ({
    meta: [
      { title: "Digital Nomad Concierge Cape Town | SALocations" },
      {
        name: "description",
        content:
          "A premium concierge service for remote workers, entrepreneurs, creators and freelancers settling into Cape Town. Accommodation, workspace setup, local support, transport, safety and trusted contacts.",
      },
      {
        property: "og:title",
        content: "Digital Nomad Concierge Cape Town | SALocations",
      },
      {
        property: "og:description",
        content:
          "Settle into Cape Town quickly, safely and stress-free. Your local concierge for accommodation, workspaces, transport, safety and trusted contacts.",
      },
      { property: "og:type", content: "website" },
      { property: "og:url", content: "/digital-nomad-concierge-cape-town" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
    links: [
      { rel: "canonical", href: "/digital-nomad-concierge-cape-town" },
    ],
  }),
  component: DigitalNomadPage,
});

const services = [
  {
    icon: "🏡",
    title: "Accommodation sourcing",
    body: "Shortlist, inspect and secure apartments, villas or boutique stays in neighbourhoods that suit your work style and lifestyle.",
  },
  {
    icon: "✈",
    title: "Airport meet & greet",
    body: "A warm welcome on arrival, private transfer to your accommodation and a quick orientation to get you settled.",
  },
  {
    icon: "📶",
    title: "SIM card & Wi-Fi setup",
    body: "Connected before you leave the airport. Backup connectivity, mobile data plans and home Wi-Fi sorted.",
  },
  {
    icon: "💻",
    title: "Home office & workspace setup",
    body: "Ergonomic furniture, monitors, lighting, power solutions and desk placement with a view.",
  },
  {
    icon: "🚗",
    title: "Car hire & local transport",
    body: "Reliable vehicle rental, driver services, parking solutions and transport advice for your stay.",
  },
  {
    icon: "🔧",
    title: "Property maintenance coordination",
    body: "A single point of contact for repairs, cleaning, gardening, security checks and any household issues.",
  },
  {
    icon: "📍",
    title: "Local recommendations & hidden gems",
    body: "Curated suggestions for restaurants, gyms, hikes, beaches, shops and experiences away from the tourist trail.",
  },
  {
    icon: "☕",
    title: "Coworking spaces & cafés",
    body: " introductions to the best coworking venues, laptop-friendly cafés and private meeting rooms.",
  },
  {
    icon: "📸",
    title: "Photography & content locations",
    body: "Scout cinematic backdrops, permits, drone-friendly locations and crew support for creators.",
  },
  {
    icon: "🌅",
    title: "Weekend adventures & day trips",
    body: "Private winelands tours, safaris, coastal drives, hiking, marine experiences and adventure planning.",
  },
  {
    icon: "🤝",
    title: "Trusted local contacts & introductions",
    body: "Connect with accountants, lawyers, creatives, wellness practitioners, fixers and business networks.",
  },
  {
    icon: "🛡️",
    title: "Safety advice & on-the-ground support",
    body: "Neighbourhood guidance, secure transport, emergency contacts and reliable support throughout your stay.",
  },
];

const forWhom = [
  "Digital nomads",
  "Remote employees",
  "Startup founders",
  "YouTubers & creators",
  "Freelancers",
  "Entrepreneurs",
  "Content teams",
  "Online coaches & consultants",
];

const process = [
  {
    n: "01",
    title: "Pre-arrival planning",
    body: "We discuss your dates, work needs, budget and preferences. I shortlist accommodation, workspaces and transport before you land.",
  },
  {
    n: "02",
    title: "Arrival & setup",
    body: "Airport pickup, SIM and Wi-Fi activation, property check-in and workspace setup completed within your first 48 hours.",
  },
  {
    n: "03",
    title: "Ongoing concierge",
    body: "WhatsApp support, local recommendations, maintenance coordination, weekend planning and trusted introductions throughout your stay.",
  },
];

function DigitalNomadPage() {
  return (
    <div className="bg-background text-foreground">
      <Nav />
      <Hero />
      <Intro />
      <Services />
      <ForWhom />
      <Process />
      <WhySAL />
      <Pricing />
      <CTA />
      <Contact />
      <Footer />
      <WhatsAppFloat />
    </div>
  );
}

function Nav() {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);
  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-all duration-500 ${
        scrolled ? "backdrop-blur-md bg-background/70 border-b border-border" : "bg-transparent"
      }`}
    >
      <div className="mx-auto flex max-w-[1600px] items-center justify-between px-6 py-5 md:px-12">
        <Link to="/" className="flex items-baseline gap-3">
          <span className="font-display text-2xl tracking-[0.18em] text-foreground">SALocations</span>
          <span className="hidden text-[10px] tracking-[0.35em] text-gold uppercase sm:inline">South Africa</span>
        </Link>

        <nav className="hidden items-center gap-10 text-xs tracking-[0.2em] uppercase text-muted-foreground md:flex">
          <a href="#about" className="hover:text-foreground transition">About</a>
          <a href="#services" className="hover:text-foreground transition">Services</a>
          <a href="#process" className="hover:text-foreground transition">How It Works</a>
          <a href="#pricing" className="hover:text-foreground transition">Pricing</a>
          <a href="#contact" className="hover:text-foreground transition">Contact</a>
        </nav>
        <a
          href="#contact"
          className="group inline-flex items-center gap-2 border border-gold/60 px-4 py-2 text-[10px] tracking-[0.3em] uppercase text-gold hover:bg-gold hover:text-background transition"
        >
          Enquire
          <span aria-hidden className="transition group-hover:translate-x-1">→</span>
        </a>
      </div>
    </header>
  );
}

function Hero() {
  return (
    <section id="top" className="relative h-[100svh] w-full overflow-hidden">
      <div className="absolute inset-0">
        <img
          src={heroImg}
          alt="Laptop on a marble desk with Table Mountain and the Atlantic Ocean visible through floor-to-ceiling windows"
          width={1920}
          height={1200}
          className="h-full w-full object-cover ken-burns"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background/60 via-background/30 to-background" />
      </div>
      <div className="relative z-10 mx-auto flex h-full max-w-[1600px] flex-col justify-end px-6 pb-20 md:px-12 md:pb-28">
        <div className="max-w-4xl fade-up">
          <div className="mb-6 flex items-center gap-4">
            <span className="h-px w-16 bg-gold" />
            <span className="eyebrow">Cape Town · Remote Work Concierge</span>
          </div>
          <h1 className="font-display text-5xl leading-[1.02] tracking-tight text-foreground sm:text-6xl md:text-7xl lg:text-[6.5rem]">
            Digital Nomad
            <br />
            <em className="not-italic text-gold">Concierge Cape Town.</em>
          </h1>
          <p className="mt-8 max-w-xl text-base leading-relaxed text-muted-foreground md:text-lg">
            Settle into Cape Town quickly, safely and stress-free. Your local partner for accommodation, workspaces, transport, safety and authentic local life.
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-4">
            <a
              href="#contact"
              className="inline-flex items-center gap-3 bg-gold px-7 py-4 text-[11px] tracking-[0.3em] uppercase text-background hover:bg-gold-soft transition"
            >
              Plan Your Arrival
              <span aria-hidden>→</span>
            </a>
            <a
              href="https://wa.me/27734921998"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-3 border border-border px-7 py-4 text-[11px] tracking-[0.3em] uppercase text-foreground hover:border-gold hover:text-gold transition"
            >
              WhatsApp Jardin
            </a>
          </div>
        </div>
      </div>
      <div className="absolute bottom-8 right-6 z-10 hidden items-center gap-3 text-[10px] tracking-[0.35em] uppercase text-muted-foreground md:right-12 md:flex">
        <span>Scroll</span>
        <span className="h-8 w-px bg-gold/60" />
      </div>
    </section>
  );
}

function Intro() {
  return (
    <section id="about" className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="grid gap-16 md:grid-cols-12">
          <div className="md:col-span-4">
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Your Local Concierge</span>
            </div>
            <h2 className="font-display text-4xl leading-tight md:text-5xl">
              Live. Work. Explore.
            </h2>
          </div>
          <div className="md:col-span-7 md:col-start-6 space-y-6 text-base leading-relaxed text-muted-foreground md:text-lg">
            <p>
              As your local Digital Nomad Concierge, I help remote workers, entrepreneurs, creators and freelancers settle into Cape Town quickly, safely and stress-free.
            </p>
            <p>
              Whether you're staying for a few weeks or several months, I'll take care of the local details so you can focus on your work while enjoying one of the world's most beautiful destinations.
            </p>
            <p>
              With years of experience in the South African film industry, location scouting, logistics and security, I know how to make your arrival and stay seamless.
            </p>
            <p className="text-foreground">
              Send me a message before you arrive in Cape Town. I'll help you hit the ground running.
            </p>
          </div>
        </div>

        <div className="mt-24 grid grid-cols-2 gap-8 border-t border-border pt-12 md:grid-cols-4 md:gap-12">
          {[
            ["2,300+", "Annual sunshine hours"],
            ["30+", "Laptop-friendly cafés"],
            ["12", "Neighbourhoods scouted"],
            ["48hrs", "Typical full setup time"],
          ].map(([n, l]) => (
            <div key={l}>
              <div className="font-display text-4xl text-gold md:text-5xl">{n}</div>
              <div className="mt-2 text-[11px] tracking-[0.3em] uppercase text-muted-foreground">
                {l}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Services() {
  return (
    <section id="services" className="relative border-t border-border bg-surface py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-20 flex flex-wrap items-end justify-between gap-8">
          <div>
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Concierge Services</span>
            </div>
            <h2 className="max-w-2xl font-display text-4xl leading-tight md:text-6xl">
              Everything you need to feel local, fast.
            </h2>
          </div>
          <p className="max-w-sm text-sm leading-relaxed text-muted-foreground">
            A complete support system for remote professionals who want to arrive focused and stay productive.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-px bg-border md:grid-cols-2 lg:grid-cols-3">
          {services.map((s, i) => (
            <article
              key={s.title}
              className="group flex flex-col bg-surface p-8 transition-colors hover:bg-surface-2 md:p-10"
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl" aria-hidden="true">
                  {s.icon}
                </span>
                <span className="font-display text-xs text-muted-foreground">
                  {String(i + 1).padStart(2, "0")}
                </span>
              </div>
              <h3 className="mt-6 font-display text-2xl leading-snug md:text-3xl">{s.title}</h3>
              <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{s.body}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function ForWhom() {
  return (
    <section className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="grid gap-16 md:grid-cols-12">
          <div className="md:col-span-5">
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Who It's For</span>
            </div>
            <h2 className="font-display text-4xl leading-tight md:text-5xl">
              Built for remote professionals who move with intention.
            </h2>
            <p className="mt-6 max-w-md text-sm leading-relaxed text-muted-foreground">
              Whether you're a solo founder, a creator, a remote team or a consultant, you get the same personal service and local intelligence.
            </p>
          </div>
          <div className="md:col-span-6 md:col-start-7">
            <div className="grid grid-cols-1 gap-px bg-border sm:grid-cols-2">
              {forWhom.map((item) => (
                <div
                  key={item}
                  className="flex items-center gap-4 bg-background p-6 text-sm text-foreground"
                >
                  <span className="h-1.5 w-1.5 rounded-full bg-gold" />
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-24 grid gap-5 md:grid-cols-3">
          <figure className="group relative overflow-hidden bg-surface">
            <div className="aspect-[4/5] overflow-hidden">
              <img
                src={accomImg}
                alt="Modern Cape Town apartment workspace with mountain views"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 group-hover:scale-105"
              />
            </div>
            <figcaption className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-background to-transparent p-6">
              <span className="eyebrow text-gold">Accommodation</span>
              <span className="mt-2 block font-display text-2xl">The right home base</span>
            </figcaption>
          </figure>
          <figure className="group relative overflow-hidden bg-surface">
            <div className="aspect-[4/5] overflow-hidden">
              <img
                src={coworkingImg}
                alt="Bright coworking cafe with people working on laptops"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 group-hover:scale-105"
              />
            </div>
            <figcaption className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-background to-transparent p-6">
              <span className="eyebrow text-gold">Workspace</span>
              <span className="mt-2 block font-display text-2xl">Where work flows</span>
            </figcaption>
          </figure>
          <figure className="group relative overflow-hidden bg-surface">
            <div className="aspect-[4/5] overflow-hidden">
              <img
                src={lifestyleImg}
                alt="Creator overlooking the Cape Town coastline with a camera"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 group-hover:scale-105"
              />
            </div>
            <figcaption className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-background to-transparent p-6">
              <span className="eyebrow text-gold">Lifestyle</span>
              <span className="mt-2 block font-display text-2xl">Adventure between calls</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>
  );
}

function Process() {
  return (
    <section id="process" className="relative border-t border-border bg-surface py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-20 text-center">
          <div className="mb-6 flex items-center justify-center gap-4">
            <span className="h-px w-10 bg-gold" />
            <span className="eyebrow">How It Works</span>
            <span className="h-px w-10 bg-gold" />
          </div>
          <h2 className="mx-auto max-w-3xl font-display text-4xl leading-tight md:text-6xl">
            Three steps to feeling at home.
          </h2>
        </div>

        <div className="grid grid-cols-1 gap-px bg-border md:grid-cols-3">
          {process.map((p) => (
            <article
              key={p.n}
              className="group relative flex flex-col bg-surface p-10 transition-colors hover:bg-surface-2"
            >
              <span className="eyebrow text-muted-foreground">Step {p.n}</span>
              <h3 className="mt-8 font-display text-2xl leading-snug md:text-3xl">{p.title}</h3>
              <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{p.body}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function WhySAL() {
  const points = [
    "Local knowledge from 20+ years in South Africa",
    "Film industry logistics and location scouting background",
    "Security-aware and safety-focused approach",
    "Trusted supplier network across Cape Town",
    "Personal, single-point-of-contact service",
    "Fast response via WhatsApp and email",
    "Creator and content-shoot friendly",
    "Flexible monthly or per-project engagement",
  ];
  return (
    <section className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto grid max-w-[1600px] gap-16 px-6 md:grid-cols-12 md:px-12">
        <div className="md:col-span-5">
          <div className="mb-6 flex items-center gap-4">
            <span className="h-px w-10 bg-gold" />
            <span className="eyebrow">Why SAL</span>
          </div>
          <h2 className="font-display text-4xl leading-tight md:text-5xl">
            The local advantage you can't book online.
          </h2>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-muted-foreground">
            I don't just arrange things — I remove friction. My background in production, security and logistics means problems get solved before you know they exist.
          </p>
        </div>
        <ul className="md:col-span-7 md:col-start-6 grid grid-cols-1 gap-px bg-border sm:grid-cols-2">
          {points.map((p, i) => (
            <li
              key={p}
              className="flex items-start gap-4 bg-background p-6 text-sm text-foreground"
            >
              <span className="mt-1 font-display text-xs text-gold">
                {String(i + 1).padStart(2, "0")}
              </span>
              <span>{p}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}

function Pricing() {
  return (
    <section id="pricing" className="relative border-t border-border bg-surface py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-20 text-center">
          <div className="mb-6 flex items-center justify-center gap-4">
            <span className="h-px w-10 bg-gold" />
            <span className="eyebrow">Engagement</span>
            <span className="h-px w-10 bg-gold" />
          </div>
          <h2 className="mx-auto max-w-3xl font-display text-4xl leading-tight md:text-6xl">
            Choose the level of support you need.
          </h2>
        </div>

        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          {[
            {
              name: "Arrival Setup",
              desc: "One-time pre-arrival and landing support.",
              features: [
                "Accommodation shortlist",
                "Airport meet & greet",
                "SIM & Wi-Fi setup",
                "Workspace setup",
                "Transport & orientation",
              ],
              cta: "Get Started",
            },
            {
              name: "Monthly Concierge",
              desc: "Ongoing local support while you're in Cape Town.",
              features: [
                "Everything in Arrival Setup",
                "WhatsApp support",
                "Maintenance coordination",
                "Local recommendations",
                "Coworking & café curation",
                "Weekend adventure planning",
              ],
              cta: "Enquire",
              featured: true,
            },
            {
              name: "Creator & Production",
              desc: "For content creators, shoots and remote teams.",
              features: [
                "Location scouting",
                "Permits & logistics",
                "Drone & crew support",
                "Transport & scheduling",
                "Local talent introductions",
              ],
              cta: "Discuss Your Project",
            },
          ].map((plan) => (
            <div
              key={plan.name}
              className={`relative flex flex-col p-10 transition ${
                plan.featured
                  ? "bg-background ring-1 ring-gold"
                  : "bg-surface-2"
              }`}
            >
              {plan.featured && (
                <span className="absolute -top-3 left-10 bg-gold px-3 py-1 text-[10px] tracking-[0.3em] uppercase text-background">
                  Most Popular
                </span>
              )}
              <h3 className="font-display text-3xl">{plan.name}</h3>
              <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{plan.desc}</p>
              <ul className="mt-8 flex-1 space-y-4 text-sm">
                {plan.features.map((f) => (
                  <li key={f} className="flex items-start gap-3">
                    <span className="mt-1.5 h-1.5 w-1.5 rounded-full bg-gold" />
                    <span>{f}</span>
                  </li>
                ))}
              </ul>
              <a
                href="#contact"
                className={`mt-10 inline-flex items-center justify-center gap-3 px-7 py-4 text-[11px] tracking-[0.3em] uppercase transition ${
                  plan.featured
                    ? "bg-gold text-background hover:bg-gold-soft"
                    : "border border-border text-foreground hover:border-gold hover:text-gold"
                }`}
              >
                {plan.cta} →
              </a>
            </div>
          ))}
        </div>

        <p className="mt-12 text-center text-sm text-muted-foreground">
          Pricing is tailored to your stay length and needs. Send a message for a personal quote.
        </p>
      </div>
    </section>
  );
}

function CTA() {
  return (
    <section className="relative border-t border-border bg-background py-32 md:py-48">
      <div className="mx-auto max-w-4xl px-6 text-center md:px-12">
        <div className="mb-8 flex items-center justify-center gap-4">
          <span className="h-px w-10 bg-gold" />
          <span className="eyebrow">Arrive Ready</span>
          <span className="h-px w-10 bg-gold" />
        </div>
        <h2 className="font-display text-5xl leading-[1.05] md:text-7xl">
          Let's make Cape Town
          <br />
          <em className="not-italic text-gold">your next base.</em>
        </h2>
        <p className="mx-auto mt-8 max-w-xl text-base leading-relaxed text-muted-foreground md:text-lg">
          Tell me your dates, your work setup and what you're looking for. I'll send a tailored plan and quote within one working day.
        </p>
        <div className="mt-12 flex flex-wrap items-center justify-center gap-4">
          <a
            href="#contact"
            className="inline-flex items-center gap-3 bg-gold px-8 py-4 text-[11px] tracking-[0.3em] uppercase text-background hover:bg-gold-soft transition"
          >
            Send Your Brief →
          </a>
          <a
            href="https://wa.me/27734921998"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-3 border border-border px-8 py-4 text-[11px] tracking-[0.3em] uppercase text-foreground hover:border-gold hover:text-gold transition"
          >
            WhatsApp +27 73 492 1998
          </a>
        </div>
      </div>
    </section>
  );
}

function Contact() {
  const formRef = useRef<HTMLFormElement>(null);
  const [sent, setSent] = useState(false);
  return (
    <section id="contact" className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto grid max-w-[1600px] gap-16 px-6 md:grid-cols-12 md:px-12">
        <div className="md:col-span-5">
          <div className="mb-6 flex items-center gap-4">
            <span className="h-px w-10 bg-gold" />
            <span className="eyebrow">Contact</span>
          </div>
          <h2 className="font-display text-4xl leading-tight md:text-5xl">
            Speak with Jardin before you arrive.
          </h2>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-muted-foreground">
            Enquiries are handled personally. Expect a considered reply, typically within one working day.
          </p>

          <dl className="mt-12 space-y-8 text-sm">
            <div>
              <dt className="eyebrow mb-2">Concierge</dt>
              <dd className="font-display text-2xl text-foreground">Jardin</dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Direct</dt>
              <dd>
                <a href="tel:+27734921998" className="text-foreground hover:text-gold transition">
                  +27 73 492 1998
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Email</dt>
              <dd>
                <a
                  href="mailto:jardin@salocations.com"
                  className="text-foreground hover:text-gold transition"
                >
                  jardin@salocations.com
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">WhatsApp</dt>
              <dd>
                <a
                  href="https://wa.me/27734921998"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-2 text-foreground hover:text-gold transition"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.134 1.585 5.929L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                  </svg>
                  Message Jardin
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Instagram</dt>
              <dd className="space-x-4 text-foreground">
                <a href="https://instagram.com/salocations" target="_blank" rel="noreferrer" className="hover:text-gold transition">
                  @salocations
                </a>
                <span className="text-border">·</span>
                <a href="https://instagram.com/capetowncompanion" target="_blank" rel="noreferrer" className="hover:text-gold transition">
                  @capetowncompanion
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Base</dt>
              <dd className="text-foreground">Cape Town, South Africa</dd>
            </div>
          </dl>
        </div>

        <form
          ref={formRef}
          onSubmit={(e) => {
            e.preventDefault();
            const data = new FormData(e.currentTarget);
            const name = data.get("name");
            const email = data.get("email");
            const arrival = data.get("arrival");
            const message = data.get("message");
            const subject = encodeURIComponent(`Digital Nomad Concierge Cape Town — ${name ?? ""}`);
            const body = encodeURIComponent(
              `Name: ${name}\nEmail: ${email}\nArrival / dates: ${arrival}\n\n${message}`,
            );
            window.location.href = `mailto:jardin@salocations.com?subject=${subject}&body=${body}`;
            setSent(true);
          }}
          className="md:col-span-6 md:col-start-7 space-y-8"
        >
          {[
            { name: "name", label: "Your Name", type: "text" },
            { name: "email", label: "Email Address", type: "email" },
            { name: "arrival", label: "Arrival Date or Month", type: "text" },
          ].map((f) => (
            <div key={f.name}>
              <label className="eyebrow mb-3 block" htmlFor={f.name}>
                {f.label}
              </label>
              <input
                id={f.name}
                name={f.name}
                type={f.type}
                required={f.name !== "arrival"}
                className="w-full border-b border-border bg-transparent py-3 text-foreground outline-none transition placeholder:text-muted-foreground focus:border-gold"
              />
            </div>
          ))}
          <div>
            <label className="eyebrow mb-3 block" htmlFor="message">
              Tell me about your stay and work needs
            </label>
            <textarea
              id="message"
              name="message"
              rows={5}
              required
              className="w-full resize-none border-b border-border bg-transparent py-3 text-foreground outline-none transition focus:border-gold"
            />
          </div>
          <button
            type="submit"
            className="inline-flex items-center gap-3 bg-gold px-8 py-4 text-[11px] tracking-[0.3em] uppercase text-background hover:bg-gold-soft transition"
          >
            {sent ? "Opening your mail…" : "Send Enquiry →"}
          </button>
        </form>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="border-t border-border bg-background py-14">
      <div className="mx-auto flex max-w-[1600px] flex-col items-center justify-between gap-6 px-6 md:flex-row md:px-12">
        <Link to="/" className="flex items-baseline gap-3">
          <span className="font-display text-xl tracking-[0.2em]">SAL</span>
          <span className="text-[10px] tracking-[0.35em] uppercase text-muted-foreground">
            Salocations · Cape Town
          </span>
        </Link>
        <p className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">
          © {new Date().getFullYear()} SALocations · Destination Experience & Marketing
        </p>
      </div>
    </footer>
  );
}
