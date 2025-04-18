import requests

def search_khan_academy(query):
    url = "https://khan-proxy.bhavjit.com/api/internal/graphql"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://www.khanacademy.org",
        "Referer": "https://www.khanacademy.org/"
    }

    payload = {
        "operationName": "videosLibrarySearch",
        "variables": {
            "query": query,
            "limit": 5
        },
        "query": """
            query videosLibrarySearch($query: String, $limit: Int) {
              videosLibrarySearch(query: $query, limit: $limit) {
                title
                url
                description
              }
            }
        """
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        videos = data.get("data", {}).get("videosLibrarySearch", [])
        results = []

        for vid in videos:
            results.append({
                "video_id": vid["url"].split("/")[-1],  # use slug as ID
                "title": vid["title"],
                "description": vid.get("description", ""),
                "url": f'https://www.khanacademy.org{vid["url"]}',
                "source": "Khan Academy"
            })

        return results

    except Exception as e:
        print("Khan Academy API error:", e)
        return []
