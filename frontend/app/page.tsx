"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [enhancedQuery, setEnhancedQuery] = useState(""); // ✅ New

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setError("");
    setResults([]);
    setEnhancedQuery("");

    try {
      const res = await fetch(`http://localhost:5000/search?q=${encodeURIComponent(query)}`);
      const data = await res.json();
      setResults(data.videos || []);
      setEnhancedQuery(data.enhanced_query || ""); // ✅ Store enhanced query
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="max-w-3xl mx-auto p-6">
      <h1 className="text-3xl font-bold text-center mb-6 text-blue-700">
        Math Video Search Engine
      </h1>

      <div className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Search for a math topic..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-grow p-3 border rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          Search
        </button>
      </div>

      {enhancedQuery && (
        <p className="text-sm text-gray-500 mb-4">
          Enhanced query: <span className="italic text-blue-700">{enhancedQuery}</span>
        </p>
      )}

      {loading && <p className="text-gray-600">Searching...</p>}
      {error && <p className="text-red-500">{error}</p>}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {results.map((video: any) => (
          <div key={video.video_id} className="p-4 border rounded shadow">
            <h2 className="font-semibold text-lg mb-1">{video.title}</h2>
            <p className="text-gray-600 mb-2">{video.description}</p>
            <a
              href={video.url || `https://www.youtube.com/watch?v=${video.video_id}`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 underline"
            >
              Watch Video ↗
            </a>
            <p className="text-sm text-gray-400 mt-1">Source: {video.source}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
