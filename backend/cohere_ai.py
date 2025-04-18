import cohere

print("✅ cohere_ai.py loaded")

COHERE_API_KEY = "7KSGzh5NWfMDBKh4vGiY58SxUWUnjWMMa95nS5rE"
co = cohere.Client(COHERE_API_KEY)

def enhance_query(query):
    try:
        response = co.generate(
            model="command",
            prompt=f"Rewrite this search query to be more specific and helpful for finding educational math videos: {query}",
            max_tokens=30,
            temperature=0.6
        )
        improved = response.generations[0].text.strip()
        print(f"🔁 Enhanced: {query} → {improved}")
        return improved
    except Exception as e:
        print("Cohere error:", e)
        return query
