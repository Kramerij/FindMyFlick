
import trm from "../images/trm.png";
import thm from "../images/thm.png";
import wicked from "../images/wicked.png";
import zoo2 from "../images/zoo2.png";

const discoverMovies = [
  { title: "TRM", img: trm },
  { title: "THM", img: thm },
  { title: "Wicked", img: wicked },
  { title: "Zoo 2", img: zoo2 },
  
];

export default function Discover() {
  return (
    <div className="p-6 max-w-6xl mx-auto text-white">
      <h2 className="text-3xl font-bold neon-text mb-6">Discover Movies</h2>
      <p className="mb-6 opacity-80">
        Explore trending, recommended, and new release movies!
      </p>

      
      <section className="flex gap-4 overflow-x-scroll scrollbar-hide pb-4">
        {discoverMovies.map((movie, i) => (
          <div
            key={i}
            className="relative min-w-[180px] h-[260px] rounded-xl overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-[0_0_20px_#ff6ed0]"
          >
            <img
              src={movie.img}
              alt={movie.title}
              className="absolute inset-0 w-full h-full object-contain"
            />
            <div className="absolute bottom-0 left-0 w-full bg-black/40 text-center p-2 neon-text font-semibold">
              {movie.title}
            </div>
          </div>
        ))}
      </section>
    </div>
  );
}
