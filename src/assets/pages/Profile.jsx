
import { useState } from "react";

export default function Profile() {
  const [profile, setProfile] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    genres: ""
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    if (formData.name && formData.email) {
      setProfile(formData);
    } else {
      alert("Please fill out your name and email.");
    }
  };

  return (
    <div className="p-6 text-white max-w-4xl mx-auto">
      <h2 className="text-3xl font-bold neon-text mb-6">Your Profile</h2>

      {profile ? (
        
        <div>
          <div className="flex items-center gap-4 mb-6">
            <div className="w-24 h-24 rounded-full bg-purple-800 flex items-center justify-center text-xl font-bold neon-text">
              {profile.name[0].toUpperCase()}
            </div>
            <div>
              <h3 className="text-xl font-semibold">{profile.name}</h3>
              <p className="opacity-80">{profile.email}</p>
              <p className="opacity-80">Favorite Genres: {profile.genres}</p>
            </div>
          </div>

          <button
            className="bg-red-700 hover:bg-red-600 px-4 py-2 rounded neon-text"
            onClick={() => setProfile(null)}
          >
            Edit Profile
          </button>
        </div>
      ) : (
        
        <div className="flex flex-col gap-4 max-w-md">
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Name"
            className="p-2 rounded text-white"
          />
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Email"
            className="p-2 rounded text-white"
          />
          <input
            type="text"
            name="genres"
            value={formData.genres}
            onChange={handleChange}
            placeholder="Favorite Genres (comma separated)"
            className="p-2 rounded text-white"
          />
          <button
            onClick={handleSave}
            className="bg-purple-700 hover:bg-purple-600 px-4 py-2 rounded neon-text"
          >
            Save Profile
          </button>
        </div>
      )}
    </div>
  );
}
