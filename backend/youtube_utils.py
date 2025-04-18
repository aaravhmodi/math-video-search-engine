import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Get the YouTube API key from the environment
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("Missing YOUTUBE_API_KEY in .env file")

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Function to search YouTube videos
def search_youtube(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=5
    )
    response = request.execute()
    results = []

    for item in response["items"]:
        results.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "source": "YouTube"
        })

    return results
