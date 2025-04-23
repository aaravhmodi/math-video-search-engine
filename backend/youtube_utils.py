import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise ValueError("Missing YOUTUBE_API_KEY in .env file")

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def search_youtube(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=15  # You can raise this up to 50 if needed
    )
    response = request.execute()
    results = []

    for item in response["items"]:
        results.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "source": "YouTube",
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })

    return results
