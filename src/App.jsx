import './App.css'

function App() {
  return (
    <>
    
      <nav className="w-full bg-black text-white px-6 py-4 flex justify-between items-center disco-glow">
        <h1 className="text-2xl font-bold tracking-wider neon-text">FindMyFlick</h1>

        <ul className="flex gap-8 text-lg font-medium">
          <li className="nav-link">Home</li>
          <li className="nav-link">Discover</li>
          <li className="nav-link">Genres</li>
          <li className="nav-link">About</li>
          <li className="nav-link">Profile</li>
        </ul>
      </nav>

     
      <header className="relative h-[300px] md:h-[450px] w-full mt-6 rounded-xl overflow-hidden shadow-xl mx-auto max-w-6xl">
        <div className="w-full h-full img-placeholder text-2xl">
          Banner Coming Soon
        </div>

        <div className="absolute inset-0 bg-black/40 flex items-center px-10">
          <div>
            <h2 className="text-4xl md:text-5xl font-bold neon-text">
              Your Movie Finder Companion
            </h2>
            <p className="mt-3 text-lg opacity-90">
              Search. Discover. Flick through your next favorite movie.
            </p>
          </div>
        </div>
      </header>

     
      <section className="mt-10 px-6 max-w-6xl mx-auto">
        <h3 className="text-2xl font-semibold mb-3 neon-text">Trending Now</h3>

        <div className="flex gap-4 overflow-x-scroll scrollbar-hide pb-4">

          {[1, 2, 3, 4].map((_, i) => (
            <div
              key={i}
              className="min-w-[180px] h-[260px] rounded-xl overflow-hidden transform hover:scale-105 transition img-placeholder"
            >
              <span className="flex items-center justify-center w-full h-full text-sm">
                Image Coming Soon
              </span>
            </div>
          ))}

        </div>
      </section>
    </>
  );
}

export default App

