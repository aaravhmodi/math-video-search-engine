from elasticsearch import Elasticsearch
import os

# Connect to local Elasticsearch (default port 9200)
from elasticsearch import Elasticsearch
import os

# Fix: Use compatible headers with newer Elasticsearch versions
es = Elasticsearch(
    "http://localhost:9200",
    headers={"Content-Type": "application/json"}  # Add this line
)


def store_video(video_id, title, description, transcript="", source="unknown", url=""):
    doc = {
        "title": title,
        "description": description,
        "transcript": transcript,
        "source": source,
        "url": url
    }
    try:
        res = es.index(index="videos", id=video_id, document=doc)
        print("📦 Document indexed:", res['result'])  # Add this line
    except Exception as e:
        print("❌ Error storing video:", e)

def search_elasticsearch(query, size=10):
    search_query = {
        "multi_match": {
            "query": query,
            "fields": ["title", "description", "transcript"]
        }
    }

    res = es.search(index="videos", body={"query": search_query}, size=size)
    hits = res.get("hits", {}).get("hits", [])
    results = []

    for hit in hits:
        source = hit["_source"]
        results.append({
            "video_id": hit["_id"],
            "title": source.get("title", ""),
            "description": source.get("description", ""),
            "url": source.get("url", ""),
            "source": source.get("source", "unknown"),
            "score": hit["_score"]
        })

    return results
