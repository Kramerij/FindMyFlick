
const genres = [
  { name: "Action", color: "bg-red-700" },
  { name: "Comedy", color: "bg-yellow-600" },
  { name: "Drama", color: "bg-purple-800" },
  { name: "Horror", color: "bg-black" },
  { name: "Sci-Fi", color: "bg-blue-800" },
  { name: "Romance", color: "bg-pink-700" },
  { name: "Animation", color: "bg-orange-500" },
  { name: "Thriller", color: "bg-indigo-900" },
];

export default function Genres() {
  return (
    <div className="p-6 max-w-6xl mx-auto text-white">
      <h2 className="text-3xl font-bold neon-text mb-6">Genres</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
        {genres.map((genre, i) => (
          <div
            key={i}
            className={`rounded-xl p-8 flex items-center justify-center font-semibold text-xl neon-text transform transition duration-300 hover:scale-105 ${genre.color}`}
          >
            {genre.name}
          </div>
        ))}
      </div>
    </div>
  );
}
