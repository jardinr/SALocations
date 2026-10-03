import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

export const Route = createFileRoute("/scouted-images-database")({
  component: ScoutedImagesDatabase,
});

const CATEGORIES = [
  "All",
  "Hero House / Character Residences",
  "Mountainside Shack / Nature Retreats",
  "Nightclub / Lounge / Beach Club",
  "Live Music Cafe & Supper Club",
  "Rehearsal & Soundstage Studios",
];

const MOCK_LOCATIONS = [
  {
    id: 1,
    name: "StarDust Theatrical Dining",
    category: "Live Music Cafe & Supper Club",
    description: "Wide timber dining floor, raised stage, grand piano. (100% Exact Match)",
    heroImage: "https://placehold.co/600x400/18181b/ffffff?text=StarDust",
    badges: ["100% Exact Match", "Scouted Images Database"],
  },
  {
    id: 2,
    name: "Harringtons Cocktail Lounge",
    category: "Nightclub / Lounge / Beach Club",
    description: "Dark mahogany wood-paneled bar counter with glowing bottle displays.",
    heroImage: "https://placehold.co/600x400/18181b/ffffff?text=Harringtons",
    badges: ["100% Exact Match", "Scouted Images Database"],
  },
  {
    id: 3,
    name: "Amara Moon",
    category: "Mountainside Shack / Nature Retreats",
    description: "Architectural timber and glass stilt retreat in Hout Bay forest.",
    heroImage: "https://placehold.co/600x400/18181b/ffffff?text=Amara+Moon",
    badges: ["Scouted Images Database"],
  },
  {
    id: 4,
    name: "Studio 107",
    category: "Rehearsal & Soundstage Studios",
    description: "Premier film soundstage and acoustic live tracking room.",
    heroImage: "https://placehold.co/600x400/18181b/ffffff?text=Studio+107",
    badges: ["Scouted Images Database"],
  },
];

function ScoutedImagesDatabase() {
  const [activeCategory, setActiveCategory] = useState("All");

  const filteredLocations =
    activeCategory === "All"
      ? MOCK_LOCATIONS
      : MOCK_LOCATIONS.filter((loc) => loc.category === activeCategory);

  return (
    <main className="min-h-screen bg-black text-white pt-24 pb-12">
      <div className="container mx-auto px-4 max-w-7xl">
        {/* Header Section */}
        <div className="mb-12">
          <h1 className="text-4xl md:text-5xl font-light mb-4 uppercase tracking-wider">
            Scouted Images Database
          </h1>
          <p className="text-zinc-400 max-w-2xl text-lg mb-6">
            Verified location inventory for SA Locations & Zencrew film production decks.
          </p>
          <div className="flex gap-4">
            <div className="bg-zinc-900 border border-zinc-800 rounded px-4 py-3">
              <div className="text-[10px] text-zinc-500 uppercase tracking-widest mb-1">
                Location Scouting & Recces
              </div>
              <div className="text-white font-medium">ZAR 5,000 / day</div>
            </div>
            <div className="bg-zinc-900 border border-zinc-800 rounded px-4 py-3">
              <div className="text-[10px] text-zinc-500 uppercase tracking-widest mb-1">
                Location Management
              </div>
              <div className="text-white font-medium">ZAR 5,500 / shoot day</div>
            </div>
          </div>
        </div>

        <Tabs defaultValue="native" className="w-full">
          <TabsList className="mb-8 bg-zinc-900 border border-zinc-800 p-1">
            <TabsTrigger
              value="native"
              className="data-[state=active]:bg-white data-[state=active]:text-black uppercase tracking-wider text-xs px-6"
            >
              Native Database
            </TabsTrigger>
            <TabsTrigger
              value="legacy"
              className="data-[state=active]:bg-white data-[state=active]:text-black uppercase tracking-wider text-xs px-6"
            >
              Google Sites Database
            </TabsTrigger>
          </TabsList>

          <TabsContent
            value="legacy"
            className="w-full h-[80vh] min-h-[600px] border border-zinc-800 rounded-lg overflow-hidden bg-white"
          >
            <iframe
              src="https://sites.google.com/view/salocations/home"
              className="w-full h-full border-none"
              title="Legacy SALocations Database"
            />
          </TabsContent>

          <TabsContent value="native">
            {/* Category Filter */}
            <div className="flex flex-wrap gap-2 mb-8">
              {CATEGORIES.map((cat) => (
                <Badge
                  key={cat}
                  variant={activeCategory === cat ? "default" : "outline"}
                  className={`cursor-pointer px-4 py-2 text-xs uppercase tracking-wider ${activeCategory === cat ? "bg-white text-black hover:bg-white/90" : "text-zinc-400 border-zinc-800 hover:text-white hover:border-zinc-500"}`}
                  onClick={() => setActiveCategory(cat)}
                >
                  {cat}
                </Badge>
              ))}
            </div>

            {/* Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredLocations.map((loc) => (
                <Card
                  key={loc.id}
                  className="bg-zinc-900 border-zinc-800 overflow-hidden group hover:border-zinc-700 transition-colors"
                >
                  <div className="aspect-[4/3] bg-zinc-800 relative overflow-hidden">
                    <img
                      src={loc.heroImage}
                      alt={loc.name}
                      className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-500 group-hover:scale-105"
                    />
                    <div className="absolute top-3 left-3 flex flex-col gap-2">
                      {loc.badges.map((badge) => (
                        <Badge
                          key={badge}
                          variant="secondary"
                          className="bg-black/90 text-white border border-white/20 uppercase tracking-widest text-[9px] px-2 py-1"
                        >
                          {badge}
                        </Badge>
                      ))}
                    </div>
                  </div>
                  <CardContent className="p-5">
                    <div className="text-[10px] text-zinc-500 uppercase tracking-widest mb-2">
                      {loc.category}
                    </div>
                    <h3 className="text-xl font-light mb-2">{loc.name}</h3>
                    <p className="text-sm text-zinc-400 line-clamp-2">{loc.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>

            <div className="mt-12 p-8 bg-zinc-900/50 border border-zinc-800/50 rounded-lg text-center flex flex-col items-center justify-center">
              <h4 className="text-xl font-light mb-2 uppercase tracking-wider text-white">
                Database Migration in Progress
              </h4>
              <p className="text-zinc-400 text-sm max-w-lg">
                Upload your scouted photos (e.g. Stardust, Harringtons, Amara Moon, Studio 107) and
                I will populate these native database entries based on our GEMINI.md protocol!
              </p>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </main>
  );
}
