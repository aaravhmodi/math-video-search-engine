from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from youtube_utils import search_youtube
from elasticsearch_utils import store_video, search_elasticsearch
from enhance_query import enhance_query

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Step 1: Enhance the query
    enhanced_query = enhance_query(query)
    print(f"🔁 Query enhanced: {query} → {enhanced_query}")

    # Step 2: Search Elasticsearch
    local_results = search_elasticsearch(enhanced_query)
    if local_results:
        print(f"✅ Found {len(local_results)} results in Elasticsearch")
        return jsonify({
            "videos": local_results,
            "enhanced_query": enhanced_query
        })

    # Step 3: Fallback to YouTube only
    youtube_results = search_youtube(enhanced_query)

    # Step 4: Store YouTube results in Elasticsearch
    for vid in youtube_results:
        store_video(
            video_id=vid["video_id"],
            title=vid["title"],
            description=vid.get("description", ""),
            transcript=vid.get("transcript", ""),
            source=vid.get("source", "YouTube"),
            url=vid.get("url", f"https://www.youtube.com/watch?v={vid['video_id']}")
        )

    print(f"🆕 Stored {len(youtube_results)} YouTube results in Elasticsearch")

    return jsonify({
        "videos": youtube_results,
        "enhanced_query": enhanced_query
    })

if __name__ == "__main__":
    app.run(debug=True)
