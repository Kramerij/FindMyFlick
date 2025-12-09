
import trm from "../images/trm.png";
import thm from "../images/thm.png";
import wicked from "../images/wicked.png";
import zoo2 from "../images/zoo2.png";

export default function Home() {
  const trendingMovies = [trm, thm, wicked, zoo2];

  return (
    <div className="text-white">
      
      <header className="relative h-[300px] md:h-[450px] w-full mt-6 rounded-xl overflow-hidden shadow-xl mx-auto max-w-6xl">
        <div className="w-full h-full img-placeholder"></div>

        <div className="absolute inset-0 bg-black/40">
          <div className="absolute top-4 left-4 z-20">
            <span className="text-lg md:text-2xl font-semibold neon-text">
              Banner Coming Soon
            </span>
          </div>

          <div className="h-full flex items-center justify-center px-6">
            <div className="text-center">
              <h2 className="text-3xl md:text-5xl font-bold neon-text">
                Your Movie Finder Companion
              </h2>
              <p className="mt-3 text-lg opacity-90">
                Search. Discover. Flick through your next favorite movie.
              </p>
            </div>
          </div>
        </div>
      </header>

      
      <section className="mt-10 px-6 max-w-6xl mx-auto">
        <h3 className="text-2xl font-semibold mb-3 neon-text">Trending Now</h3>

        <div className="flex gap-4 overflow-x-scroll scrollbar-hide pb-4">
          {trendingMovies.map((img, i) => (
            <div
              key={i}
              className="relative min-w-[180px] h-[260px] rounded-xl overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-[0_0_20px_#ff6ed0] bg-black"
            >
              <img
                src={img}
                alt={`Movie poster ${i + 1}`}
                className="absolute inset-0 w-full h-full object-contain"
              />
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
