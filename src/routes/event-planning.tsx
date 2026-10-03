import { createFileRoute } from "@tanstack/react-router";
import { Link } from "@tanstack/react-router";
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";

import bella1 from "@/assets/exp-bellaev.jpg";
import bella2 from "@/assets/gal-bellaev-2.jpg";
import bella3 from "@/assets/gal-bellaev-3.jpg";
import bella4 from "@/assets/gal-bellaev-4.jpg";
import bella5 from "@/assets/gal-bellaev-5.jpg";

export const Route = createFileRoute("/event-planning")({
  component: EventPlanning,
});

const venues = [
  {
    id: "bella-ev",
    name: "Bella Ev Seminar Room",
    type: "Intimate Seminars & Workshops",
    description: "An elegantly appointed seminar space perfect for intimate corporate retreats, masterclasses, and private workshops. Features classic architecture, ample natural light, and refined antique furnishings.",
    images: [bella1, bella2, bella3, bella4, bella5],
  }
];

function EventPlanning() {
  return (
    <main className="min-h-screen bg-black text-white pt-24 pb-20">
      <div className="container mx-auto px-4 max-w-[1200px]">
        
        {/* Header Section */}
        <div className="mb-20 pt-10 text-center">
          <Badge className="bg-gold/10 text-[#d4af37] hover:bg-gold/20 border-[#d4af37]/50 mb-6 uppercase tracking-widest px-4 py-1">
            08. Core Discipline
          </Badge>
          <h1 className="text-4xl md:text-6xl font-light mb-6 uppercase tracking-widest font-display">Event Planning</h1>
          <p className="text-zinc-400 max-w-2xl mx-auto text-lg leading-relaxed">
            From venue sourcing and digital marketing to ticket sales and cinematic event coverage. We curate and manage bespoke events in Cape Town's most exclusive spaces.
          </p>
          <div className="mt-10 flex flex-wrap justify-center gap-4">
             <a href="#contact" className="inline-flex items-center justify-center border border-[#d4af37] px-8 py-3 text-xs tracking-[0.2em] uppercase text-[#d4af37] hover:bg-[#d4af37] hover:text-black transition">
               Inquire Now
             </a>
             <Link to="/" className="inline-flex items-center justify-center border border-zinc-800 px-8 py-3 text-xs tracking-[0.2em] uppercase text-zinc-400 hover:text-white transition bg-zinc-900/50">
               Back Home
             </Link>
          </div>
        </div>

        {/* Venues Section */}
        <div className="space-y-32">
          <div className="flex items-center gap-4 mb-16 opacity-70">
            <span className="h-px w-10 bg-white" />
            <span className="text-xs uppercase tracking-[0.3em]">Featured Venues</span>
            <span className="h-px flex-1 bg-white/10" />
          </div>

          {venues.map((venue) => (
            <div key={venue.id} className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20 items-center">
              
              {/* Text Side */}
              <div className="lg:col-span-5 order-2 lg:order-1">
                <div className="text-[10px] text-zinc-500 uppercase tracking-[0.3em] mb-4">
                  {venue.type}
                </div>
                <h2 className="text-3xl md:text-4xl font-light mb-6">{venue.name}</h2>
                <p className="text-zinc-400 leading-relaxed mb-8">
                  {venue.description}
                </p>
                <Dialog>
                  <DialogTrigger asChild>
                    <button className="group inline-flex items-center gap-3 text-xs tracking-[0.2em] uppercase text-white hover:text-[#d4af37] transition">
                      <span className="border-b border-[#d4af37]/50 pb-1">View Full Gallery</span>
                      <span className="transition-transform group-hover:translate-x-2">→</span>
                    </button>
                  </DialogTrigger>
                  <DialogContent className="max-w-[95vw] md:max-w-5xl bg-black/95 border-zinc-800 p-0 overflow-hidden">
                    <Carousel className="w-full">
                      <CarouselContent>
                        {venue.images.map((img, idx) => (
                          <CarouselItem key={idx}>
                            <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center p-4">
                              <img src={img} alt={`${venue.name} - Image ${idx + 1}`} className="max-w-full max-h-[85vh] object-contain shadow-2xl" />
                            </div>
                          </CarouselItem>
                        ))}
                      </CarouselContent>
                      <CarouselPrevious className="left-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
                      <CarouselNext className="right-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
                    </Carousel>
                  </DialogContent>
                </Dialog>
              </div>

              {/* Image Side */}
              <div className="lg:col-span-7 order-1 lg:order-2 relative">
                <Dialog>
                  <DialogTrigger asChild>
                    <div className="aspect-[4/3] overflow-hidden bg-zinc-900 cursor-pointer group relative">
                      <img 
                        src={venue.images[0]} 
                        alt={venue.name} 
                        className="w-full h-full object-cover transition duration-1000 group-hover:scale-105 opacity-80 group-hover:opacity-100" 
                      />
                      <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center">
                        <span className="text-white text-sm font-medium tracking-[0.3em] uppercase mb-2">View Gallery</span>
                        <span className="text-white/80 text-[10px] tracking-widest uppercase">({venue.images.length} Photos)</span>
                      </div>
                    </div>
                  </DialogTrigger>
                  <DialogContent className="max-w-[95vw] md:max-w-5xl bg-black/95 border-zinc-800 p-0 overflow-hidden">
                    <Carousel className="w-full">
                      <CarouselContent>
                        {venue.images.map((img, idx) => (
                          <CarouselItem key={idx}>
                            <div className="aspect-[4/3] md:aspect-[16/9] w-full flex items-center justify-center p-4">
                              <img src={img} alt={`${venue.name} - Image ${idx + 1}`} className="max-w-full max-h-[85vh] object-contain shadow-2xl" />
                            </div>
                          </CarouselItem>
                        ))}
                      </CarouselContent>
                      <CarouselPrevious className="left-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
                      <CarouselNext className="right-4 bg-black/50 border-white/20 text-white hover:bg-black/70 hover:text-white" />
                    </Carousel>
                  </DialogContent>
                </Dialog>

                {/* Decorative image offsets */}
                <div className="hidden md:block absolute -bottom-10 -left-10 w-48 aspect-[3/4] border border-white/10 p-2 bg-black z-10 shadow-2xl">
                   <img src={venue.images[1]} alt="Detail" className="w-full h-full object-cover opacity-80" />
                </div>
              </div>

            </div>
          ))}

          {/* Add more venues placeholder */}
          <div className="py-20 text-center border border-dashed border-white/10 bg-zinc-950">
             <h3 className="text-xl font-light text-zinc-500 uppercase tracking-widest mb-4">More Venues Coming Soon</h3>
             <p className="text-zinc-600 text-sm max-w-md mx-auto">Upload more venue photos to have them featured in your Event Planning portfolio.</p>
          </div>

        </div>
      </div>
    </main>
  );
}
