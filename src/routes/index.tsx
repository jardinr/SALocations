import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import heroImg from "@/assets/hero-capetown.jpg";
import expSafari from "@/assets/exp-safari.jpg";
import expHeli from "@/assets/exp-heli.jpg";
import expWine from "@/assets/exp-wine.jpg";
import expFilm from "@/assets/exp-film.jpg";
import galLeopard from "@/assets/gal-leopard.jpg";
import galVilla from "@/assets/gal-villa.jpg";
import galDining from "@/assets/gal-dining.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "SAL — Experience South Africa Beyond the Brochure" },
      {
        name: "description",
        content:
          "SALocations — a Cape Town based Destination Experience & Marketing Company crafting bespoke luxury journeys, production logistics and concierge across South Africa.",
      },
      { property: "og:title", content: "SAL — Experience South Africa Beyond the Brochure" },
      {
        property: "og:description",
        content:
          "Bespoke luxury experiences, destination marketing, production logistics and concierge services across South Africa.",
      },
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
  },
  {
    n: "02",
    title: "Luxury Concierge",
    body: "Private villas, executive transport, helicopters, private aviation, yachts, private chefs and VIP security.",
  },
  {
    n: "03",
    title: "Production Support",
    body: "Location scouting, film permits, production logistics, equipment, crew and drone operations.",
  },
  {
    n: "04",
    title: "Luxury Content Creation",
    body: "Commercial photography, cinematic film, drone content, destination documentaries and brand storytelling.",
  },
  {
    n: "05",
    title: "Adventure Experiences",
    body: "Private safaris, marine journeys, wine estates, mountain expeditions and conservation immersions.",
  },
  {
    n: "06",
    title: "Destination Marketing",
    body: "Tourism campaigns, brand partnerships, digital strategy and AI Search, SEO and GEO optimisation.",
  },
];

const signature = [
  { title: "Luxury Cape Town Collection", tag: "City & Coast", img: heroImg },
  { title: "Private Winelands Escape", tag: "Franschhoek · Stellenbosch", img: expWine },
  { title: "Helicopter & Yacht Experience", tag: "Atlantic Seaboard", img: expHeli },
  { title: "Ultimate Safari Journey", tag: "Sabi Sand · Kruger", img: expSafari },
  { title: "Creator Experience South Africa", tag: "Content & Brand", img: expFilm },
  { title: "Conservation Expedition", tag: "Wilderness Access", img: galLeopard },
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
      <Marquee />
      <WhyUs />
      <Gallery />
      <Testimonials />
      <CTA />
      <Contact />
      <Footer />
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
        <a href="#top" className="flex items-baseline gap-2">
          <span className="font-display text-2xl tracking-[0.2em] text-foreground">SAL</span>
          <span className="hidden text-[10px] tracking-[0.35em] text-muted-foreground uppercase sm:inline">
            Salocations
          </span>
        </a>
        <nav className="hidden items-center gap-10 text-xs tracking-[0.2em] uppercase text-muted-foreground md:flex">
          <a href="#about" className="hover:text-foreground transition">About</a>
          <a href="#services" className="hover:text-foreground transition">Services</a>
          <a href="#experiences" className="hover:text-foreground transition">Experiences</a>
          <a href="#journal" className="hover:text-foreground transition">Journal</a>
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
              photography, videography and AI-powered marketing to create unforgettable journeys
              for discerning international clients.
            </p>
            <p>
              With decades of experience across the South African film industry, security
              operations and luxury hospitality partnerships, SAL provides exclusive access to
              people, places and experiences that most visitors never discover.
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
              Six disciplines. One quiet standard of excellence.
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
              className="group relative bg-surface p-10 transition-colors hover:bg-surface-2"
            >
              <div className="flex items-center justify-between">
                <span className="eyebrow">{s.n}</span>
                <span
                  aria-hidden
                  className="text-gold opacity-0 transition-all group-hover:translate-x-1 group-hover:opacity-100"
                >
                  →
                </span>
              </div>
              <h3 className="mt-10 font-display text-2xl leading-snug md:text-3xl">{s.title}</h3>
              <p className="mt-4 text-sm leading-relaxed text-muted-foreground">{s.body}</p>
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
                  {String(active + 1).padStart(2, "0")} / {String(signature.length).padStart(2, "0")}
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
                  className={`group flex w-full items-center justify-between border-t border-border py-6 text-left transition ${
                    i === active ? "text-foreground" : "text-muted-foreground"
                  } ${i === signature.length - 1 ? "border-b" : ""}`}
                >
                  <span className="flex items-baseline gap-6">
                    <span className="eyebrow text-muted-foreground">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <span className="font-display text-2xl md:text-3xl">{s.title}</span>
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

function Marquee() {
  return (
    <section className="relative border-y border-border bg-surface py-8 overflow-hidden">
      <div className="flex whitespace-nowrap animate-[scroll_45s_linear_infinite] will-change-transform">
        {[...clients, ...clients].map((c, i) => (
          <span
            key={i}
            className="mx-10 font-display text-2xl text-muted-foreground md:text-4xl"
          >
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
          <figure className="col-span-12 md:col-span-8">
            <div className="aspect-[16/10] overflow-hidden bg-surface">
              <img src={galVilla} alt="Cliffside villa above Cape Town at twilight" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Camps Bay</span><span>Private Villa</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-[3/4] overflow-hidden bg-surface">
              <img src={galLeopard} alt="Leopard portrait at dawn" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Sabi Sand</span><span>Wildlife</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img src={expWine} alt="Cape Winelands estate at sunset" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Franschhoek</span><span>Wine Estate</span>
            </figcaption>
          </figure>
          <figure className="col-span-6 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img src={expHeli} alt="Helicopter and yacht off the Atlantic seaboard" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Atlantic Seaboard</span><span>Charters</span>
            </figcaption>
          </figure>
          <figure className="col-span-12 md:col-span-4">
            <div className="aspect-square overflow-hidden bg-surface">
              <img src={galDining} alt="Fine dining plated course" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Cape Town</span><span>Fine Dining</span>
            </figcaption>
          </figure>
          <figure className="col-span-12 md:col-span-8">
            <div className="aspect-[16/9] overflow-hidden bg-surface">
              <img src={expFilm} alt="Film crew at a cliff-top location at sunset" loading="lazy" className="h-full w-full object-cover transition duration-700 hover:scale-105" />
            </div>
            <figcaption className="mt-3 flex justify-between text-[11px] tracking-[0.25em] uppercase text-muted-foreground">
              <span>Chapman's Peak</span><span>Production</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>
  );
}

function Testimonials() {
  const [i, setI] = useState(0);
  const t = testimonials[i];
  return (
    <section className="relative overflow-hidden border-t border-border py-28 md:py-40">
      <div className="pointer-events-none absolute inset-0 opacity-40">
        <img src={expSafari} alt="" className="h-full w-full object-cover" loading="lazy" />
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
                <a href="tel:+27734921998" className="text-foreground hover:text-gold transition">
                  +27 73 492 1998
                </a>
              </dd>
            </div>
            <div>
              <dt className="eyebrow mb-2">Email</dt>
              <dd>
                <a
                  href="mailto:info@salocations.com"
                  className="text-foreground hover:text-gold transition"
                >
                  info@salocations.com
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
              <dt className="eyebrow mb-2">Studio</dt>
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
            const message = data.get("message");
            const subject = encodeURIComponent(`SAL enquiry — ${name ?? ""}`);
            const body = encodeURIComponent(
              `Name: ${name}\nEmail: ${email}\n\n${message}`,
            );
            window.location.href = `mailto:info@salocations.com?subject=${subject}&body=${body}`;
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
        <p className="text-[10px] tracking-[0.3em] uppercase text-muted-foreground">
          © {new Date().getFullYear()} SALocations · Destination Experience & Marketing
        </p>
      </div>
    </footer>
  );
}
