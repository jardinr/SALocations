import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import heroImgUrl from "@/assets/hero-tablemountain-new.jpg";
import cliftonImgUrl from "@/assets/gal-clifton.jpg";
import llandudnoImgUrl from "@/assets/gal-llandudno.jpg";
import campsbayImgUrl from "@/assets/sig-campsbay.jpg";
import reverieImgUrl from "@/assets/gal-reverie.jpg";
import campsbaySunsetUrl from "@/assets/gal-campsbay-sunset.jpg";
import campsbayProm1Url from "@/assets/gal-campsbay-prom1.jpg";
import campsbayProm2Url from "@/assets/gal-campsbay-prom2.jpg";
import campsbayProm3Url from "@/assets/gal-campsbay-prom3.jpg";

import expSafari from "@/assets/exp-safari.jpg";
import expHeli from "@/assets/exp-heli.jpg";
import expWine from "@/assets/exp-wine.jpg";
import expFilm from "@/assets/exp-film.jpg";
import galLeopard from "@/assets/gal-leopard.jpg";
import sigWinelands from "@/assets/sig-winelands.jpg";
import sigHeli from "@/assets/sig-heli.jpg";
import sigSafari from "@/assets/sig-safari.jpg";
import sigCreator from "@/assets/sig-creator.jpg";
import sigConservation from "@/assets/sig-conservation.jpg";
import sigStargazing from "@/assets/sig-stargazing.jpg";
import dnHero from "@/assets/dn-hero.jpg";
import antPenguins from "@/assets/ant-penguins.jpg";
import destMarketing from "@/assets/dest-marketing.jpg";
import prodSupport from "@/assets/prod-support.jpg";
import expSaBg from "@/assets/exp-sa-bg.jpg";
import antJet from "@/assets/ant-jet.jpg";
import antCamp from "@/assets/ant-camp.jpg";
import expBellaEv from "@/assets/exp-bellaev.jpg";
import heroBokaapPano from "@/assets/hero-bokaap-pano.jpg";

import antHero from "@/assets/ant-hero.jpg";
import { WhatsAppFloat } from "@/components/WhatsAppFloat";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
  type CarouselApi,
} from "@/components/ui/carousel";
import {
  Youtube,
  Instagram,
  Phone,
  Mail,
  MessageCircle,
  Play,
  ExternalLink,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";

const heroAsset = { url: heroImgUrl };
const cliftonAsset = { url: cliftonImgUrl };
const llandudnoAsset = { url: llandudnoImgUrl };
const campsbayAsset = { url: campsbayImgUrl };
const reverieAsset = { url: reverieImgUrl };
const campsbaySunsetAsset = { url: campsbaySunsetUrl };
const campsbayProm1Asset = { url: campsbayProm1Url };
const campsbayProm2Asset = { url: campsbayProm2Url };
const campsbayProm3Asset = { url: campsbayProm3Url };
const heroImg = heroAsset.url;

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "SALocations | Bespoke Luxury Journeys" },
      {
        name: "description",
        content:
          "SALocations designs bespoke luxury journeys, film production logistics, concierge services and destination marketing across South Africa.",
      },
      { property: "og:title", content: "SALocations | Bespoke Luxury Journeys" },
      {
        property: "og:description",
        content:
          "SALocations designs bespoke luxury journeys, film production logistics, concierge services and destination marketing across South Africa.",
      },
      { property: "og:image", content: "https://www.salocations.com/favicon.jpg" },
      { property: "og:url", content: "/" },
    ],
    links: [{ rel: "canonical", href: "/" }],
  }),
  component: Index,
});

const services = [
  {
    n: "01",
    title: "Destination Experience Design",
    body: "Tailor-made South African itineraries blending luxury, adventure, culture and conservation.",
    img: expSaBg,
  },
  {
    n: "02",
    title: "Luxury Concierge",
    body: "Private villas, executive transport, helicopters, private aviation, yachts, private chefs and VIP security.",
    img: expHeli,
  },
  {
    n: "03",
    title: "Production Support",
    body: "Location scouting, film permits, production logistics, equipment, crew and drone operations.",
    img: prodSupport,
  },
  {
    n: "04",
    title: "Luxury Content Creation",
    body: "Commercial photography, cinematic film, drone content, destination documentaries and brand storytelling.",
    img: heroBokaapPano,
    link: "#drone-showcase",
  },
  {
    n: "05",
    title: "Adventure Experiences",
    body: "Private safaris, marine journeys, wine estates, remote star gazing, mountain expeditions and conservation immersions.",
    img: expSafari,
  },
  {
    n: "06",
    title: "Destination Marketing",
    body: "Tourism campaigns, brand partnerships, digital strategy and AI Search, SEO and GEO optimisation.",
    img: destMarketing,
  },
  {
    n: "07",
    title: "Digital Nomad Concierge",
    body: "Cape Town relocation support for remote workers: accommodation, workspaces, SIMs, transport and local safety.",
    img: dnHero,
    link: "/digital-nomad-concierge-cape-town",
  },
  {
    n: "08",
    title: "Event Planning",
    body: "Venue sourcing, ticket sales, marketing, and event photo/videography. Featuring premier locations like Bella Ev.",
    img: expBellaEv,
    link: "/event-planning",
  },
  {
    n: "09",
    title: "Bespoke Property Sales",
    body: "Exclusive investment and retirement property sourcing. Curated high-yield real estate and luxury coastal homes.",
    img: sigWinelands,
  },
];

const signature = [
  { title: "Luxury Cape Town Collection", tag: "City & Coast", img: campsbayAsset.url },
  { title: "Private Winelands Escape", tag: "Franschhoek · Stellenbosch", img: sigWinelands },
  { title: "Helicopter & Yacht Experience", tag: "Atlantic Seaboard", img: sigHeli },
  { title: "Ultimate Safari Journey", tag: "Sabi Sand · Kruger", img: sigSafari },
  {
    title: "Star Gazing at Remote Locations",
    tag: "Karoo · Cederberg · Namakwa",
    img: sigStargazing,
  },
  { title: "Creator Experience South Africa", tag: "Content & Brand", img: sigCreator },
  { title: "Conservation Expedition", tag: "Wilderness Access", img: sigConservation },
];

const droneVideos = [
  {
    id: "PJZ2LxqFs1Q",
    n: "01",
    title: "Du Kloof Lodge & Bainskloof Pass",
    location: "Du Toitskloof Pass",
    region: "Limietberg Nature Reserve · Paarl & Worcester",
    duration: "2:46",
    body: "Dramatic sandstone amphitheaters, crystal mountain streams, and the serpentine cliff curves of Bainskloof Pass captured in cinematic 4K aerial footage.",
    thumb: "https://img.youtube.com/vi/PJZ2LxqFs1Q/maxresdefault.jpg",
    youtubeUrl: "https://www.youtube.com/watch?v=PJZ2LxqFs1Q",
  },
  {
    id: "a9KmbtJNiNE",
    n: "02",
    title: "Hout Bay From Above",
    location: "Hout Bay Harbour & Sentinel",
    region: "Atlantic Seaboard · Cape Peninsula",
    duration: "6:19",
    body: "Sweeping bird's-eye views across the active fishing harbour, rolling ocean swells, and the towering sentinel cliffs guarding the Atlantic ocean bay.",
    thumb: "https://img.youtube.com/vi/a9KmbtJNiNE/maxresdefault.jpg",
    youtubeUrl: "https://www.youtube.com/watch?v=a9KmbtJNiNE",
  },
  {
    id: "9S0nYthsCBc",
    n: "03",
    title: "Suikerbossie Pass & Ocean Overlook",
    location: "Suikerbossie Ridge",
    region: "Victoria Road · Atlantic Ocean & Chapman's Peak Vista",
    duration: "1:38",
    body: "Breathtaking coastal ridge drone cinematography capturing the iconic pass between Camps Bay and Hout Bay with panoramic Atlantic horizons.",
    thumb: "https://img.youtube.com/vi/9S0nYthsCBc/maxresdefault.jpg",
    youtubeUrl: "https://www.youtube.com/watch?v=9S0nYthsCBc",
  },
];

const clients = [
  "Luxury Travellers",
  "UHNW Individuals",
  "Film & Television",
  "Content Creators",
  "Professional Athletes",
  "Sports Organisations",
  "Travel Advisors",
  "Hospitality Brands",
];

const testimonials = [
  {
    quote:
      "SAL opened doors we didn't know existed. Every moment felt handcrafted — from the helicopter transfer to the private chef under the stars.",
    name: "Private Client",
    role: "London",
  },
  {
    quote:
      "An extraordinary production partner. Permits, locations, crew, security — handled with quiet precision on a demanding schedule.",
    name: "Executive Producer",
    role: "New York",
  },
  {
    quote:
      "The most considered destination team in South Africa. They understand luxury the way it should be understood: personal, discreet, unforgettable.",
    name: "Family Office",
    role: "Zurich",
  },
];

function Index() {
  return (
    <div className="bg-background text-foreground">
      <Nav />
      <Hero />
      <About />
      <Services />
      <Signature />
      <Antarctic />
      <Marquee />
      <WhyUs />
      <Gallery />
      <DroneVideoCarousel />
      <Testimonials />
      <FAQ />
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
        <a href="#top" className="flex items-baseline gap-3">
          <span className="font-display text-2xl tracking-[0.18em] text-foreground">
            SALocations
          </span>
          <span className="hidden text-[10px] tracking-[0.35em] text-gold uppercase sm:inline">
            South Africa
          </span>
        </a>

        <nav className="hidden items-center gap-6 text-xs tracking-[0.2em] uppercase text-muted-foreground lg:flex">
          <a href="#about" className="hover:text-foreground transition">
            About
          </a>
          <a href="#services" className="hover:text-foreground transition">
            Services
          </a>
          <a href="#experiences" className="hover:text-foreground transition">
            Experiences
          </a>
          <Link
            to="/digital-nomad-concierge-cape-town"
            className="hover:text-foreground transition"
          >
            Nomad
          </Link>
          <Link to="/scouted-images-database" className="hover:text-foreground transition">
            Database
          </Link>
          <a href="#drone-showcase" className="hover:text-foreground transition">
            Drone Reel
          </a>
          <a href="#antarctic" className="hover:text-foreground transition">
            Antarctic
          </a>
          <a href="#contact" className="hover:text-foreground transition">
            Contact
          </a>
        </nav>
        <a
          href="#contact"
          className="group inline-flex items-center gap-2 border border-gold/60 px-4 py-2 text-[10px] tracking-[0.3em] uppercase text-gold hover:bg-gold hover:text-background transition"
        >
          Enquire
          <span aria-hidden className="transition group-hover:translate-x-1">
            →
          </span>
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
          alt="Table Mountain silhouette over Cape Town at golden hour"
          width={1920}
          height={1200}
          className="h-full w-full object-cover ken-burns"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background/50 via-background/20 to-background" />
      </div>
      <div className="relative z-10 mx-auto flex h-full max-w-[1600px] flex-col justify-end px-6 pb-20 md:px-12 md:pb-28">
        <div className="max-w-4xl fade-up">
          <div className="mb-6 flex items-center gap-4">
            <span className="h-px w-16 bg-gold" />
            <span className="eyebrow">South Africa · Est. Cape Town</span>
          </div>
          <h1 className="font-display text-5xl leading-[1.02] tracking-tight text-foreground sm:text-6xl md:text-7xl lg:text-[6.5rem]">
            Experience South Africa
            <br />
            <em className="not-italic text-gold">Beyond the Brochure.</em>
          </h1>
          <p className="mt-8 max-w-xl text-base leading-relaxed text-muted-foreground md:text-lg">
            Bespoke luxury experiences, destination marketing, production logistics and concierge
            services — crafted for those who travel differently.
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-4">
            <a
              href="#contact"
              className="inline-flex items-center gap-3 bg-gold px-7 py-4 text-[11px] tracking-[0.3em] uppercase text-background hover:bg-gold-soft transition"
            >
              Plan Your Experience
              <span aria-hidden>→</span>
            </a>
            <a
              href="#experiences"
              className="inline-flex items-center gap-3 border border-border px-7 py-4 text-[11px] tracking-[0.3em] uppercase text-foreground hover:border-gold hover:text-gold transition"
            >
              Signature Journeys
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

function About() {
  return (
    <section id="about" className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="grid gap-16 md:grid-cols-12">
          <div className="md:col-span-4">
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">The House of SAL</span>
            </div>
            <h2 className="font-display text-4xl leading-tight md:text-5xl">
              A destination partner, not a tour operator.
            </h2>
          </div>
          <div className="md:col-span-7 md:col-start-6 space-y-6 text-base leading-relaxed text-muted-foreground md:text-lg">
            <p>
              SAL is a Cape Town based Destination Experience & Marketing Company that designs,
              delivers and markets extraordinary South African experiences.
            </p>
            <p>
              We combine destination expertise, luxury concierge, film production logistics,
              photography, videography and AI-powered marketing to create unforgettable journeys for
              discerning international clients.
            </p>
            <p>
              With decades of experience across the South African film industry, security operations
              and luxury hospitality partnerships, SAL provides exclusive access to people, places
              and experiences that most visitors never discover.
            </p>
            <p className="text-foreground">
              Experiences designed to be lived, captured and remembered.
            </p>
          </div>
        </div>

        <div className="mt-24 grid grid-cols-2 gap-8 border-t border-border pt-12 md:grid-cols-4 md:gap-12">
          {[
            ["20+", "Years in country"],
            ["150+", "Trusted suppliers"],
            ["40+", "Productions supported"],
            ["9", "Provinces, one team"],
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
              <span className="eyebrow">Core Services</span>
            </div>
            <h2 className="max-w-2xl font-display text-4xl leading-tight md:text-6xl">
              Nine disciplines. One quiet standard of excellence.
            </h2>
          </div>
          <p className="max-w-sm text-sm leading-relaxed text-muted-foreground">
            From private itineraries to international productions, every engagement is led by a
            senior partner and delivered with operational precision.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-px bg-border md:grid-cols-2 lg:grid-cols-3">
          {services.map((s) => (
            <article
              key={s.n}
              className="group relative flex flex-col bg-surface transition-colors hover:bg-surface-2"
            >
              <div className="relative aspect-[16/10] w-full overflow-hidden bg-surface-2">
                <img
                  src={s.img}
                  alt={s.title}
                  loading="lazy"
                  className="h-full w-full object-cover opacity-80 transition duration-700 group-hover:scale-[1.03] group-hover:opacity-100"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-surface via-surface/40 to-transparent" />
                <span className="absolute left-6 top-6 eyebrow bg-background/40 px-2 py-1 backdrop-blur-sm">
                  {s.n}
                </span>
              </div>
              <div className="flex flex-1 flex-col p-10">
                <div className="flex items-center justify-between">
                  <span className="eyebrow text-muted-foreground">Discipline</span>
                  {s.link ? (
                    <Link
                      to={s.link}
                      className="text-gold opacity-0 transition-all group-hover:translate-x-1 group-hover:opacity-100 text-[10px] tracking-[0.3em] uppercase"
                    >
                      View →
                    </Link>
                  ) : (
                    <span
                      aria-hidden
                      className="text-gold opacity-0 transition-all group-hover:translate-x-1 group-hover:opacity-100"
                    >
                      →
                    </span>
                  )}
                </div>
                <h3 className="mt-6 font-display text-2xl leading-snug md:text-3xl">
                  {s.link ? (
                    <Link to={s.link} className="hover:text-gold transition">
                      {s.title}
                    </Link>
                  ) : (
                    s.title
                  )}
                </h3>
                <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{s.body}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function Signature() {
  const [active, setActive] = useState(0);
  return (
    <section id="experiences" className="relative border-t border-border py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-16 flex items-end justify-between gap-8">
          <div>
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Signature Experiences</span>
            </div>
            <h2 className="max-w-3xl font-display text-4xl leading-tight md:text-6xl">
              Journeys built around the moments most will never see.
            </h2>
          </div>
        </div>

        <div className="grid gap-10 lg:grid-cols-12">
          <div className="relative lg:col-span-7">
            <div className="relative aspect-[4/5] w-full overflow-hidden bg-surface lg:aspect-[5/6]">
              {signature.map((s, i) => (
                <img
                  key={s.title}
                  src={s.img}
                  alt={s.title}
                  loading="lazy"
                  className={`absolute inset-0 h-full w-full object-cover transition-opacity duration-700 ${
                    i === active ? "opacity-100" : "opacity-0"
                  }`}
                />
              ))}
              <div className="absolute inset-0 bg-gradient-to-t from-background/70 to-transparent" />
              <div className="absolute bottom-8 left-8 right-8 flex items-end justify-between text-foreground">
                <div>
                  <div className="eyebrow mb-3">{signature[active].tag}</div>
                  <div className="font-display text-2xl md:text-3xl">{signature[active].title}</div>
                </div>
                <div className="font-display text-sm text-gold">
                  {String(active + 1).padStart(2, "0")} /{" "}
                  {String(signature.length).padStart(2, "0")}
                </div>
              </div>
            </div>
          </div>

          <ul className="lg:col-span-5">
            {signature.map((s, i) => (
              <li key={s.title}>
                <button
                  type="button"
                  onMouseEnter={() => setActive(i)}
                  onFocus={() => setActive(i)}
                  onClick={() => setActive(i)}
                  className={`group flex w-full items-center justify-between gap-4 border-t border-border py-5 text-left transition ${
                    i === active ? "text-foreground" : "text-muted-foreground"
                  } ${i === signature.length - 1 ? "border-b" : ""}`}
                >
                  <span className="flex flex-1 items-center gap-5">
                    <span
                      className={`relative h-16 w-24 shrink-0 overflow-hidden bg-surface-2 transition ${
                        i === active ? "ring-1 ring-gold" : "opacity-70 group-hover:opacity-100"
                      }`}
                    >
                      <img
                        src={s.img}
                        alt={s.title}
                        loading="lazy"
                        className="h-full w-full object-cover"
                      />
                    </span>
                    <span className="flex flex-col gap-1">
                      <span className="eyebrow text-muted-foreground">
                        {String(i + 1).padStart(2, "0")} · {s.tag}
                      </span>
                      <span className="font-display text-xl leading-tight md:text-2xl">
                        {s.title}
                      </span>
                    </span>
                  </span>
                  <span
                    aria-hidden
                    className={`text-gold transition ${
                      i === active ? "translate-x-1 opacity-100" : "opacity-40"
                    }`}
                  >
                    →
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

function Antarctic() {
  const journeys = [
    {
      n: "01",
      title: "Emperor Penguin Expedition",
      tag: "Weddell Sea · November",
      body: "Fly deep into the interior to walk among an emperor penguin colony — a rare privilege granted to only a handful of travellers each year.",
      img: antPenguins,
    },
    {
      n: "02",
      title: "South Pole Private Charter",
      tag: "90°S · Ceremonial Pole",
      body: "A private jet flight from Cape Town to the white continent, culminating at the geographic South Pole with SAL's expedition team.",
      img: antJet,
    },
    {
      n: "03",
      title: "Ultima Wilderness Camp",
      tag: "Wolf's Fang · Queen Maud Land",
      body: "Heated sleeping pods beneath 3,000m granite spires — climbing, ski touring, ice caves and aurora watching from a private base camp.",
      img: antCamp,
    },
  ];
  return (
    <section
      id="antarctic"
      className="relative overflow-hidden border-t border-border bg-background py-28 md:py-40"
    >
      <div className="pointer-events-none absolute inset-0">
        <img
          src={antHero}
          alt="Antarctic Expedition"
          loading="lazy"
          className="h-full w-full object-cover opacity-40"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background via-background/70 to-background" />
      </div>

      <div className="relative mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-16 grid gap-10 md:grid-cols-12">
          <div className="md:col-span-6">
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">New Frontier · Antarctica</span>
            </div>
            <h2 className="font-display text-4xl leading-[1.05] md:text-6xl">
              From Cape Town
              <br />
              <em className="not-italic text-gold">to the white continent.</em>
            </h2>
          </div>
          <div className="md:col-span-5 md:col-start-8 space-y-6 text-base leading-relaxed text-muted-foreground md:text-lg">
            <p>
              Cape Town is the natural gateway to Antarctica. In partnership with the continent's
              most established private operators, SAL curates fly-in expeditions to the last true
              wilderness on earth.
            </p>
            <p>
              Private jet transfers, heated wilderness camps, emperor penguin encounters, ski
              touring, ice climbing and a landing at the geographic South Pole — arranged with the
              same discretion as every SAL journey.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 gap-px bg-border md:grid-cols-3">
          {journeys.map((j) => (
            <article
              key={j.n}
              className="group relative flex flex-col bg-background transition-colors hover:bg-surface"
            >
              <div className="relative aspect-[4/5] w-full overflow-hidden">
                <img
                  src={j.img}
                  alt={j.title}
                  loading="lazy"
                  className="h-full w-full object-cover transition duration-700 group-hover:scale-[1.04]"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-background via-background/30 to-transparent" />
                <span className="absolute left-6 top-6 eyebrow bg-background/50 px-2 py-1 backdrop-blur-sm">
                  {j.n} · {j.tag}
                </span>
              </div>
              <div className="flex flex-1 flex-col p-8">
                <h3 className="font-display text-2xl leading-snug md:text-3xl">{j.title}</h3>
                <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{j.body}</p>
                <a
                  href="#contact"
                  className="mt-8 inline-flex items-center gap-2 text-[10px] tracking-[0.3em] uppercase text-gold hover:text-gold-soft transition"
                >
                  Enquire
                  <span aria-hidden className="transition group-hover:translate-x-1">
                    →
                  </span>
                </a>
              </div>
            </article>
          ))}
        </div>

        <div className="mt-16 grid gap-6 border-t border-border pt-12 text-sm text-muted-foreground md:grid-cols-4">
          {[
            ["5hr", "Cape Town → Wolf's Fang"],
            ["−20°C", "Summer daytime average"],
            ["24hr", "Daylight, Nov – Jan"],
            ["12", "Guests per departure"],
          ].map(([n, l]) => (
            <div key={l}>
              <div className="font-display text-3xl text-foreground md:text-4xl">{n}</div>
              <div className="mt-2 text-[11px] tracking-[0.3em] uppercase">{l}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Marquee() {
  return (
    <section className="relative border-y border-border bg-surface py-8 overflow-hidden">
      <div className="flex whitespace-nowrap animate-[scroll_45s_linear_infinite] will-change-transform">
        {[...clients, ...clients].map((c, i) => (
          <span key={i} className="mx-10 font-display text-2xl text-muted-foreground md:text-4xl">
            {c} <span className="mx-6 text-gold">✦</span>
          </span>
        ))}
      </div>
      <style>{`@keyframes scroll { from { transform: translateX(0) } to { transform: translateX(-50%) } }`}</style>
    </section>
  );
}

function WhyUs() {
  const points = [
    "Local expertise, international standards",
    "Two decades in the SA film industry",
    "Luxury hospitality partnerships",
    "Security & logistics specialists",
    "Exclusive access, quietly arranged",
    "In-house photography & film",
    "AI-powered destination marketing",
    "A single point of contact, always",
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
            The difference is in what you don't see.
          </h2>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-muted-foreground">
            Precision, discretion and access — refined over two decades operating at the highest
            levels of hospitality, production and security in South Africa.
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

function Gallery() {
  return (
    <section id="journal" className="relative border-t border-border bg-background py-28 md:py-40">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        <div className="mb-16 flex flex-wrap items-end justify-between gap-6">
          <div>
            <div className="mb-6 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Gallery</span>
            </div>
            <h2 className="max-w-2xl font-display text-4xl leading-tight md:text-6xl">
              A country, captured.
            </h2>
          </div>
          <p className="max-w-sm text-sm leading-relaxed text-muted-foreground">
            Moments from Cape Town, the Winelands, the Kruger and beyond — photographed and filmed
            by our production team.
          </p>
        </div>

        <div className="grid grid-cols-12 gap-3 md:gap-5">
          <Dialog>
            <DialogTrigger asChild>
              <figure className="col-span-12 md:col-span-8 cursor-pointer group">
                <div className="aspect-[16/10] overflow-hidden bg-surface relative">
                  <img
                    src={campsbaySunsetAsset.url}
                    alt="Camps Bay sunset"
                    loading="lazy"
                    className="h-full w-full object-cover transition duration-700 group-hover:scale-105"
                  />
                  <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center">
                    <span className="text-white text-sm font-medium tracking-widest uppercase mb-2">
                      View Gallery
                    </span>
                    <span className="text-white/80 text-xs">(4 Photos)</span>
                  </div>
                </div>
                <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
                  <span>Camps Bay</span>
                  <span>Promenade</span>
                </figcaption>
              </figure>
            </DialogTrigger>
            <DialogContent className="max-w-[95vw] md:max-w-5xl bg-black/95 border-zinc-800 p-0 overflow-hidden">
              <Carousel className="w-full">
                <CarouselContent>
                  <CarouselItem>
                    <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center">
                      <img
                        src={campsbaySunsetAsset.url}
                        alt="Camps Bay sunset"
                        className="max-w-full max-h-[85vh] object-contain"
                      />
                    </div>
                  </CarouselItem>
                  <CarouselItem>
                    <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center">
                      <img
                        src={campsbayProm1Asset.url}
                        alt="Camps Bay promenade"
                        className="max-w-full max-h-[85vh] object-contain"
                      />
                    </div>
                  </CarouselItem>
                  <CarouselItem>
                    <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center">
                      <img
                        src={campsbayProm2Asset.url}
                        alt="Camps Bay promenade"
                        className="max-w-full max-h-[85vh] object-contain"
                      />
                    </div>
                  </CarouselItem>
                  <CarouselItem>
                    <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center">
                      <img
                        src={campsbayProm3Asset.url}
                        alt="Camps Bay promenade"
                        className="max-w-full max-h-[85vh] object-contain"
                      />
                    </div>
                  </CarouselItem>
                </CarouselContent>
                <CarouselPrevious className="left-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
                <CarouselNext className="right-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
              </Carousel>
            </DialogContent>
          </Dialog>
          <figure className="col-span-12">
            <div className="aspect-[21/9] md:aspect-[32/9] overflow-hidden bg-surface">
              <img
                src={cliftonAsset.url}
                alt="Clifton 4th beach panorama with Lion's Head"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Atlantis Dunes</span>
              <span>West Coast</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-[3/4] overflow-hidden bg-surface">
              <img
                src={galLeopard}
                alt="Leopard portrait at dawn"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Sabi Sand</span>
              <span>Wildlife</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img
                src={expWine}
                alt="Cape Winelands estate at sunset"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Franschhoek</span>
              <span>Wine Estate</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img
                src={expHeli}
                alt="Helicopter and yacht off the Atlantic seaboard"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Atlantic Seaboard</span>
              <span>Charters</span>
            </figcaption>
          </figure>
          <figure className="col-span-12 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img
                src={llandudnoAsset.url}
                alt="Llandudno coastal vista"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Llandudno</span>
              <span>View</span>
            </figcaption>
          </figure>
          <figure className="col-span-12 md:col-span-8">
            <div className="aspect-[16/9] overflow-hidden bg-surface">
              <img
                src={expFilm}
                alt="Film crew at a cliff-top location at sunset"
                loading="lazy"
                className="h-full w-full object-cover transition duration-700 hover:scale-105"
              />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Chapman's Peak</span>
              <span>Production</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>
  );
}

function DroneVideoCarousel() {
  const [activeVideo, setActiveVideo] = useState<(typeof droneVideos)[0] | null>(null);
  const [api, setApi] = useState<CarouselApi>();
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    if (!api) return;
    setCurrent(api.selectedScrollSnap());
    api.on("select", () => {
      setCurrent(api.selectedScrollSnap());
    });
  }, [api]);

  return (
    <section id="drone-showcase" className="relative border-t border-border py-28 md:py-36 bg-surface/20">
      <div className="mx-auto max-w-[1600px] px-6 md:px-12">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-8 mb-14">
          <div className="max-w-2xl">
            <div className="mb-4 flex items-center gap-4">
              <span className="h-px w-10 bg-gold" />
              <span className="eyebrow">Aerial Cinematography</span>
            </div>
            <h2 className="font-display text-4xl leading-tight md:text-5xl text-foreground">
              Best Drone Locations
            </h2>
            <p className="mt-4 text-sm md:text-base leading-relaxed text-muted-foreground">
              From soaring sandstone passes and deep river ravines to panoramic Atlantic coastal ridges,
              explore our signature Cape Town and Western Cape filming locations captured from above.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-4">
            <a
              href="https://www.youtube.com/@salocations"
              target="_blank"
              rel="noreferrer"
              className="group inline-flex items-center gap-2.5 rounded-full border border-border bg-surface px-5 py-2.5 text-xs uppercase tracking-wider text-foreground hover:border-[#FF0000] hover:text-white hover:bg-[#FF0000]/10 transition-all"
            >
              <Youtube className="h-4 w-4 text-[#FF0000] transition-transform group-hover:scale-110" />
              <span>YouTube Channel</span>
              <ExternalLink className="h-3 w-3 text-muted-foreground group-hover:text-white" />
            </a>

            {/* Slider Navigation Buttons */}
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => api?.scrollPrev()}
                aria-label="Previous drone video"
                className="flex h-10 w-10 items-center justify-center rounded-full border border-border bg-surface text-foreground transition-all hover:border-gold hover:text-gold active:scale-95"
              >
                <ChevronLeft className="h-5 w-5" />
              </button>
              <button
                type="button"
                onClick={() => api?.scrollNext()}
                aria-label="Next drone video"
                className="flex h-10 w-10 items-center justify-center rounded-full border border-border bg-surface text-foreground transition-all hover:border-gold hover:text-gold active:scale-95"
              >
                <ChevronRight className="h-5 w-5" />
              </button>
            </div>
          </div>
        </div>

        {/* Carousel */}
        <Carousel
          setApi={setApi}
          opts={{
            align: "start",
            loop: true,
          }}
          className="w-full"
        >
          <CarouselContent className="-ml-4 md:-ml-6">
            {droneVideos.map((video) => (
              <CarouselItem
                key={video.id}
                className="pl-4 md:pl-6 basis-[90%] sm:basis-[75%] md:basis-[50%] lg:basis-1/3"
              >
                <div className="group relative flex h-full flex-col overflow-hidden rounded-xl border border-border/80 bg-surface/50 backdrop-blur-sm transition-all duration-500 hover:border-gold/60 hover:bg-surface/80 hover:shadow-2xl hover:shadow-gold/5">
                  {/* Video Thumbnail / Preview Trigger */}
                  <div
                    onClick={() => setActiveVideo(video)}
                    className="relative aspect-video w-full cursor-pointer overflow-hidden bg-black"
                  >
                    <img
                      src={video.thumb}
                      alt={video.title}
                      loading="lazy"
                      className="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
                    />
                    {/* Ambient vignette */}
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-black/20 opacity-90 transition-opacity group-hover:opacity-75" />

                    {/* Top location tag */}
                    <div className="absolute left-4 top-4 flex items-center gap-2">
                      <span className="rounded-full bg-black/70 backdrop-blur-md border border-white/10 px-3 py-1 text-[10px] tracking-[0.2em] uppercase text-gold font-medium">
                        {video.n} · {video.location}
                      </span>
                    </div>

                    {/* Duration badge */}
                    <div className="absolute right-4 top-4">
                      <span className="rounded-full bg-black/70 backdrop-blur-md border border-white/10 px-2.5 py-1 text-[10px] tracking-wider text-white/90">
                        {video.duration}
                      </span>
                    </div>

                    {/* Central Play Trigger */}
                    <div className="absolute inset-0 flex items-center justify-center">
                      <div className="flex h-14 w-14 items-center justify-center rounded-full bg-gold/90 text-background shadow-2xl backdrop-blur-md transition-all duration-300 group-hover:scale-110 group-hover:bg-gold group-hover:shadow-[0_0_30px_rgba(201,168,76,0.6)]">
                        <Play className="h-6 w-6 fill-current translate-x-0.5" />
                      </div>
                    </div>
                  </div>

                  {/* Card Content */}
                  <div className="flex flex-1 flex-col justify-between p-6">
                    <div>
                      <div className="text-[10px] tracking-[0.3em] uppercase text-gold font-medium">
                        {video.region}
                      </div>
                      <h3 className="mt-2 font-display text-xl text-foreground group-hover:text-gold transition-colors">
                        {video.title}
                      </h3>
                      <p className="mt-3 text-xs leading-relaxed text-muted-foreground">
                        {video.body}
                      </p>
                    </div>

                    <div className="mt-6 pt-5 border-t border-border/60 flex items-center justify-between gap-3">
                      <button
                        type="button"
                        onClick={() => setActiveVideo(video)}
                        className="inline-flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-gold hover:text-gold-soft transition font-medium"
                      >
                        <Play className="h-3.5 w-3.5 fill-current" />
                        Watch Drone Reel
                      </button>

                      <a
                        href={video.youtubeUrl}
                        target="_blank"
                        rel="noreferrer"
                        title="Watch on YouTube"
                        className="flex h-8 w-8 items-center justify-center rounded-full border border-border bg-surface text-muted-foreground transition hover:border-[#FF0000] hover:text-[#FF0000] hover:bg-[#FF0000]/10"
                      >
                        <Youtube className="h-3.5 w-3.5" />
                      </a>
                    </div>
                  </div>
                </div>
              </CarouselItem>
            ))}
          </CarouselContent>
        </Carousel>

        {/* Carousel Pagination Dots */}
        <div className="mt-8 flex items-center justify-center gap-2">
          {droneVideos.map((_, index) => (
            <button
              key={index}
              type="button"
              onClick={() => api?.scrollTo(index)}
              className={`h-1.5 transition-all rounded-full ${
                current === index ? "w-8 bg-gold" : "w-2.5 bg-border hover:bg-muted-foreground"
              }`}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </div>

      {/* Video Modal Player */}
      <Dialog open={!!activeVideo} onOpenChange={(open) => !open && setActiveVideo(null)}>
        <DialogContent className="max-w-[95vw] md:max-w-4xl bg-black/95 border-zinc-800 p-0 overflow-hidden shadow-2xl">
          {activeVideo && (
            <div>
              <div className="relative aspect-video w-full bg-black">
                <iframe
                  src={`https://www.youtube-nocookie.com/embed/${activeVideo.id}?autoplay=1&rel=0`}
                  title={activeVideo.title}
                  className="h-full w-full border-0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  allowFullScreen
                />
              </div>
              <div className="p-6 md:p-8 flex flex-col md:flex-row md:items-center justify-between gap-6 border-t border-zinc-800 bg-surface/60">
                <div>
                  <div className="flex items-center gap-2 mb-1.5">
                    <span className="eyebrow text-gold">{activeVideo.location}</span>
                    <span className="text-zinc-600">·</span>
                    <span className="text-xs text-muted-foreground">{activeVideo.duration}</span>
                  </div>
                  <h3 className="font-display text-xl md:text-2xl text-foreground">
                    {activeVideo.title}
                  </h3>
                  <p className="mt-1.5 text-xs md:text-sm text-muted-foreground max-w-xl">
                    {activeVideo.body}
                  </p>
                </div>
                <div className="flex items-center gap-3 shrink-0">
                  <a
                    href={activeVideo.youtubeUrl}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex items-center gap-2 rounded-full border border-red-500/40 bg-red-500/10 px-5 py-2.5 text-xs uppercase tracking-wider text-white hover:bg-red-500 hover:border-red-500 transition-all font-medium"
                  >
                    <Youtube className="h-4 w-4 text-red-500 hover:text-white" />
                    Watch on YouTube
                  </a>
                </div>
              </div>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </section>
  );
}

function Testimonials() {
  const [i, setI] = useState(0);
  const t = testimonials[i];
  return (
    <section className="relative overflow-hidden border-t border-border py-28 md:py-40">
      <div className="pointer-events-none absolute inset-0 opacity-40">
        <img src={expSafari} alt="Luxury South African safari experience" className="h-full w-full object-cover" loading="lazy" />
        <div className="absolute inset-0 bg-background/85" />
      </div>
      <div className="relative mx-auto max-w-4xl px-6 text-center md:px-12">
        <div className="mb-8 flex items-center justify-center gap-4">
          <span className="h-px w-10 bg-gold" />
          <span className="eyebrow">In their words</span>
          <span className="h-px w-10 bg-gold" />
        </div>
        <blockquote className="font-display text-2xl leading-snug md:text-4xl">
          <span className="text-gold">“</span>
          {t.quote}
          <span className="text-gold">”</span>
        </blockquote>
        <div className="mt-10 text-[11px] tracking-[0.35em] uppercase text-muted-foreground">
          {t.name} · {t.role}
        </div>
        <div className="mt-10 flex items-center justify-center gap-3">
          {testimonials.map((_, k) => (
            <button
              key={k}
              onClick={() => setI(k)}
              aria-label={`Testimonial ${k + 1}`}
              className={`h-px transition-all ${
                k === i ? "w-10 bg-gold" : "w-6 bg-border hover:bg-muted-foreground"
              }`}
            />
          ))}
        </div>
      </div>
    </section>
  );
}

function FAQ() {
  const faqs = [
    {
      q: "What is SALocations?",
      a: "SALocations is a premier luxury travel, film production, and concierge agency based in Cape Town, South Africa. We specialize in curating bespoke destination experiences, providing seamless production logistics, and offering exclusive access to high-yield investment properties and private adventures across Southern Africa and Antarctica."
    },
    {
      q: "How do I book a private safari or luxury journey in South Africa?",
      a: "You can book a private luxury journey by contacting our founder directly through our website. We handle every detail from VIP security and executive transport to private villas and exclusive marine expeditions, ensuring a seamless and discreet experience tailored to your specific requirements. We partner with the official authorities like South African National Parks to ensure compliance."
    },
    {
      q: "What production support services do you offer for filming in Cape Town?",
      a: "We provide comprehensive film production support in Cape Town, including location scouting, securing film permits via the City of Cape Town Film Office, managing production logistics, and arranging elite equipment, crew, and drone operations. With over two decades of industry experience, we guarantee operational precision for international campaigns."
    },
    {
      q: "Can SALocations assist with event planning and bespoke property sales?",
      a: "Yes, SALocations offers comprehensive event planning, from venue sourcing at premier locations like Bella Ev to cinematic event coverage. We also specialize in bespoke property sales, sourcing exclusive investment and retirement properties, including high-yield real estate and luxury coastal homes."
    }
  ];

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faqs.map(faq => ({
      "@type": "Question",
      "name": faq.q,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": faq.a
      }
    }))
  };

  return (
    <section className="relative border-t border-border py-28 md:py-40 bg-background">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
      <div className="mx-auto max-w-4xl px-6 md:px-12">
        <div className="mb-16 flex items-center justify-center gap-4">
          <span className="h-px w-10 bg-gold" />
          <span className="eyebrow uppercase tracking-[0.3em] text-gold">Common Questions</span>
          <span className="h-px w-10 bg-gold" />
        </div>
        <h2 className="font-display text-4xl leading-tight md:text-5xl text-center mb-16">
          Answers to your questions.
        </h2>
        <div className="space-y-12">
          {faqs.map((faq, i) => (
            <div key={i} className="border-b border-border pb-8">
              <h3 className="font-display text-2xl mb-4 text-foreground">{faq.q}</h3>
              <p className="text-muted-foreground leading-relaxed text-sm max-w-3xl">
                {faq.a}
              </p>
            </div>
          ))}
        </div>
        
        {/* Author / Publisher signals & External Links for GEO */}
        <div className="mt-20 border-t border-white/5 pt-12 text-xs text-muted-foreground max-w-2xl text-center mx-auto space-y-4">
          <p>
            <strong>Author:</strong> Jardin Roestorff (Founder). Our services comply with local regulations.
          </p>
          <p>
            For external resources, please refer to the <a href="https://www.sanparks.org/" target="_blank" rel="noopener noreferrer" className="underline hover:text-gold">South African National Parks</a> and the <a href="https://www.capetown.gov.za/work%20and%20business/film-in-cape-town" target="_blank" rel="noopener noreferrer" className="underline hover:text-gold">Cape Town Film Permit Office</a>.
          </p>
        </div>
      </div>
    </section>
  );
}

function CTA() {
  return (
    <section className="relative border-t border-border bg-surface py-32 md:py-48">
      <div className="mx-auto max-w-4xl px-6 text-center md:px-12">
        <div className="mb-8 flex items-center justify-center gap-4">
          <span className="h-px w-10 bg-gold" />
          <span className="eyebrow">Begin</span>
          <span className="h-px w-10 bg-gold" />
        </div>
        <h2 className="font-display text-5xl leading-[1.05] md:text-7xl">
          Let's create your
          <br />
          <em className="not-italic text-gold">South African experience.</em>
        </h2>
        <p className="mx-auto mt-8 max-w-xl text-base leading-relaxed text-muted-foreground md:text-lg">
          Whether you're planning a luxury holiday, an international production, a sporting
          engagement or a bespoke expedition, SAL will design and deliver it.
        </p>
        <div className="mt-12 flex flex-wrap items-center justify-center gap-4">
          <a
            href="#contact"
            className="inline-flex items-center gap-3 bg-gold px-8 py-4 text-[11px] tracking-[0.3em] uppercase text-background hover:bg-gold-soft transition"
          >
            Plan Your Experience →
          </a>
          <a
            href="#contact"
            className="inline-flex items-center gap-3 border border-border px-8 py-4 text-[11px] tracking-[0.3em] uppercase text-foreground hover:border-gold hover:text-gold transition"
          >
            Partner With SAL
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
            Speak with our founder.
          </h2>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-muted-foreground">
            Enquiries are handled personally. Expect a considered reply, typically within one
            working day.
          </p>

          <dl className="mt-12 space-y-8 text-sm">
            <div>
              <dt className="eyebrow mb-2">Founder</dt>
              <dd className="font-display text-2xl text-foreground">Jardin</dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Direct</dt>
              <dd>
                <a
                  href="tel:+27734921998"
                  className="group inline-flex items-center gap-2.5 rounded-full border border-border/80 bg-surface/50 px-4 py-2 text-xs uppercase tracking-wider text-foreground hover:border-gold hover:text-gold hover:bg-gold/10 transition-all"
                >
                  <Phone className="h-4 w-4 text-gold transition-transform group-hover:scale-110" />
                  +27 73 492 1998
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Email</dt>
              <dd>
                <a
                  href="mailto:jardin@salocations.com"
                  className="group inline-flex items-center gap-2.5 rounded-full border border-border/80 bg-surface/50 px-4 py-2 text-xs uppercase tracking-wider text-foreground hover:border-gold hover:text-gold hover:bg-gold/10 transition-all"
                >
                  <Mail className="h-4 w-4 text-gold transition-transform group-hover:scale-110" />
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
                  className="group inline-flex items-center gap-2.5 rounded-full border border-border/80 bg-surface/50 px-4 py-2 text-xs uppercase tracking-wider text-foreground hover:border-[#25D366]/60 hover:text-[#25D366] hover:bg-[#25D366]/10 transition-all"
                >
                  <MessageCircle className="h-4 w-4 text-[#25D366] transition-transform group-hover:scale-110" />
                  Message Jardin
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Location</dt>
              <dd>
                <span className="text-foreground">
                  Cape Town, South Africa
                </span>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Instagram</dt>
              <dd className="flex flex-wrap items-center gap-3 text-foreground">
                <a
                  href="https://instagram.com/salocations"
                  target="_blank"
                  rel="noreferrer"
                  className="group inline-flex items-center gap-2 rounded-full border border-border/80 bg-surface/50 px-3.5 py-1.5 text-xs text-foreground hover:border-[#E1306C]/60 hover:text-white hover:bg-[#E1306C]/10 transition-all"
                >
                  <Instagram className="h-3.5 w-3.5 text-[#E1306C] transition-transform group-hover:scale-110" />
                  @salocations
                </a>
                <a
                  href="https://instagram.com/capetowncompanion"
                  target="_blank"
                  rel="noreferrer"
                  className="group inline-flex items-center gap-2 rounded-full border border-border/80 bg-surface/50 px-3.5 py-1.5 text-xs text-foreground hover:border-[#E1306C]/60 hover:text-white hover:bg-[#E1306C]/10 transition-all"
                >
                  <Instagram className="h-3.5 w-3.5 text-[#E1306C] transition-transform group-hover:scale-110" />
                  @capetowncompanion
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">YouTube</dt>
              <dd>
                <a
                  href="https://www.youtube.com/@salocations"
                  target="_blank"
                  rel="noreferrer"
                  className="group inline-flex items-center gap-2.5 rounded-full border border-border/80 bg-surface/50 px-4 py-2 text-xs uppercase tracking-wider text-foreground hover:border-[#FF0000]/60 hover:text-white hover:bg-[#FF0000]/10 transition-all"
                >
                  <Youtube className="h-4 w-4 text-[#FF0000] transition-transform group-hover:scale-110" />
                  @salocations · YouTube Channel
                </a>
              </dd>
            </div>
          </dl>

          <div className="mt-10 pt-8 border-t border-border/60">
            <span className="eyebrow block mb-3 text-muted-foreground">Direct Social Channels</span>
            <div className="flex flex-wrap items-center gap-3">
              <a
                href="https://www.youtube.com/@salocations"
                target="_blank"
                rel="noreferrer"
                aria-label="SALocations on YouTube"
                title="YouTube: @salocations"
                className="group flex h-10 items-center gap-2 rounded-full border border-border bg-surface px-4 text-xs text-foreground transition-all hover:border-[#FF0000] hover:bg-[#FF0000]/10 hover:text-white hover:scale-105"
              >
                <Youtube className="h-4 w-4 text-[#FF0000] transition-transform group-hover:scale-110" />
                <span>YouTube</span>
              </a>
              <a
                href="https://instagram.com/salocations"
                target="_blank"
                rel="noreferrer"
                aria-label="SALocations on Instagram"
                title="Instagram: @salocations"
                className="group flex h-10 items-center gap-2 rounded-full border border-border bg-surface px-4 text-xs text-foreground transition-all hover:border-[#E1306C] hover:bg-[#E1306C]/10 hover:text-white hover:scale-105"
              >
                <Instagram className="h-4 w-4 text-[#E1306C] transition-transform group-hover:scale-110" />
                <span>Instagram</span>
              </a>
              <a
                href="https://wa.me/27734921998"
                target="_blank"
                rel="noreferrer"
                aria-label="WhatsApp Concierge"
                title="WhatsApp: +27 73 492 1998"
                className="group flex h-10 items-center gap-2 rounded-full border border-border bg-surface px-4 text-xs text-foreground transition-all hover:border-[#25D366] hover:bg-[#25D366]/10 hover:text-[#25D366] hover:scale-105"
              >
                <MessageCircle className="h-4 w-4 text-[#25D366] transition-transform group-hover:scale-110" />
                <span>WhatsApp</span>
              </a>
              <a
                href="tel:+27734921998"
                aria-label="Call Direct"
                title="Call: +27 73 492 1998"
                className="group flex h-10 items-center gap-2 rounded-full border border-border bg-surface px-4 text-xs text-foreground transition-all hover:border-gold hover:bg-gold/10 hover:text-gold hover:scale-105"
              >
                <Phone className="h-4 w-4 text-gold transition-transform group-hover:scale-110" />
                <span>Phone</span>
              </a>
              <a
                href="mailto:jardin@salocations.com"
                aria-label="Email Concierge"
                title="Email: jardin@salocations.com"
                className="group flex h-10 items-center gap-2 rounded-full border border-border bg-surface px-4 text-xs text-foreground transition-all hover:border-gold hover:bg-gold/10 hover:text-gold hover:scale-105"
              >
                <Mail className="h-4 w-4 text-gold transition-transform group-hover:scale-110" />
                <span>Email</span>
              </a>
            </div>
          </div>
        </div>

        <form
          ref={formRef}
          onSubmit={(e) => {
            e.preventDefault();
            const data = new FormData(e.currentTarget);
            const name = data.get("name");
            const email = data.get("email");
            const message = data.get("message");
            const subject = encodeURIComponent(`SAL enquiry — ${name ?? ""}`);
            const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`);
            window.location.href = `mailto:jardin@salocations.com?subject=${subject}&body=${body}`;
            setSent(true);
          }}
          className="md:col-span-6 md:col-start-7 space-y-8"
        >
          {[
            { name: "name", label: "Your Name", type: "text" },
            { name: "email", label: "Email Address", type: "email" },
            { name: "interest", label: "Interest — Travel, Production, Partnership", type: "text" },
          ].map((f) => (
            <div key={f.name}>
              <label className="eyebrow mb-3 block" htmlFor={f.name}>
                {f.label}
              </label>
              <input
                id={f.name}
                name={f.name}
                type={f.type}
                required={f.name !== "interest"}
                className="w-full border-b border-border bg-transparent py-3 text-foreground outline-none transition placeholder:text-muted-foreground focus:border-gold"
              />
            </div>
          ))}
          <div>
            <label className="eyebrow mb-3 block" htmlFor="message">
              Tell us about your project
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
        <div className="flex items-baseline gap-3">
          <span className="font-display text-xl tracking-[0.2em]">SAL</span>
          <span className="text-[10px] tracking-[0.35em] uppercase text-muted-foreground">
            Salocations · Cape Town
          </span>
        </div>

        {/* Social Icon Buttons in Footer */}
        <div className="flex items-center gap-3">
          <a
            href="https://www.youtube.com/@salocations"
            target="_blank"
            rel="noreferrer"
            aria-label="SALocations on YouTube"
            title="YouTube: @salocations"
            className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface/80 text-muted-foreground transition-all hover:border-[#FF0000] hover:bg-[#FF0000]/10 hover:text-[#FF0000] hover:scale-105"
          >
            <Youtube className="h-4 w-4" />
          </a>
          <a
            href="https://instagram.com/salocations"
            target="_blank"
            rel="noreferrer"
            aria-label="SALocations on Instagram"
            title="Instagram: @salocations"
            className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface/80 text-muted-foreground transition-all hover:border-[#E1306C] hover:bg-[#E1306C]/10 hover:text-[#E1306C] hover:scale-105"
          >
            <Instagram className="h-4 w-4" />
          </a>
          <a
            href="https://wa.me/27734921998"
            target="_blank"
            rel="noreferrer"
            aria-label="WhatsApp Concierge"
            title="WhatsApp: +27 73 492 1998"
            className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface/80 text-muted-foreground transition-all hover:border-[#25D366] hover:bg-[#25D366]/10 hover:text-[#25D366] hover:scale-105"
          >
            <MessageCircle className="h-4 w-4" />
          </a>
          <a
            href="tel:+27734921998"
            aria-label="Call Direct"
            title="Direct: +27 73 492 1998"
            className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface/80 text-muted-foreground transition-all hover:border-gold hover:bg-gold/10 hover:text-gold hover:scale-105"
          >
            <Phone className="h-4 w-4" />
          </a>
          <a
            href="mailto:jardin@salocations.com"
            aria-label="Email Concierge"
            title="Email: jardin@salocations.com"
            className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface/80 text-muted-foreground transition-all hover:border-gold hover:bg-gold/10 hover:text-gold hover:scale-105"
          >
            <Mail className="h-4 w-4" />
          </a>
        </div>

        <p className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">
          © {new Date().getFullYear()} SALocations · Destination Experience & Marketing
        </p>
      </div>
    </footer>
  );
}
