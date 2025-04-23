import requests

def search_khan_academy(query, limit=10):
    url = f"https://khan-api.bhavjit.com/api/search?q={query}&limit={limit}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        results = []

        for video in data:
            results.append({
                "video_id": video.get("youtube_id", video.get("id")),
                "title": video.get("title", ""),
                "description": video.get("description", ""),
                "url": f"https://www.khanacademy.org{video['url']}" if "url" in video else "",
                "source": "Khan Academy"
            })

        print(f"🎓 Fetched {len(results)} Khan Academy videos")
        return results

    except Exception as e:
        print("❌ Khan Academy API error:", e)
        return []
