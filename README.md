# 📚 Math Video Search Engine

A full-stack educational search engine that helps students find the most relevant **YouTube math tutorial videos**, enhanced with AI-powered query understanding and local indexing using **Elasticsearch**.

![screenshot](https://img.freepik.com/premium-vector/mathematics-word-concepts-banner-presentation-website-isolated-lettering-typography-idea-with-linear-icons-algebra-geometry-statistics-basic-maths-vector-outline-illustration_106317-8216.jpg?w=2000)

---

## 🚀 Features

- 🔍 **AI Query Enhancement**: Improves vague or short queries using a local NLP model (`sentence-transformers`).
- 🎥 **YouTube API Integration**: Fetches real-time math tutorial videos.
- 📦 **Elasticsearch Indexing**: Stores and retrieves videos for faster future searches.
- 🌐 **Next.js Frontend**: Beautiful, responsive UI for search interaction.
- 🧠 **Smart Fallback**: If no local results are found, fetches new ones from YouTube and stores them.

---

## 🛠️ Tech Stack

| Frontend       | Backend       | AI / Search      | Deployment       |
|----------------|----------------|------------------|------------------|
| Next.js (React) | Flask (Python) | Elasticsearch    | Render / GitHub  |
| Tailwind CSS   | REST API       | sentence-transformers | Docker (Optional) |
