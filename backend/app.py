from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from youtube_utils import search_youtube
from khan_utils import search_khan_academy
from elasticsearch_utils import store_video, search_elasticsearch
# from huggingface_utils import enhance_query
from enhance_query import enhance_query


# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Step 1: Use Hugging Face to enhance query
    enhanced_query = enhance_query(query)
    print(f"🔁 Query enhanced: {query} → {enhanced_query}")

    # Step 2: Search in Elasticsearch first
    local_results = search_elasticsearch(enhanced_query)
    if local_results:
        print(f"✅ Found {len(local_results)} results in Elasticsearch")
        return jsonify({
            "videos": local_results,
            "enhanced_query": enhanced_query
        })

    # Step 3: Fallback to YouTube + Khan if nothing found
    youtube_results = search_youtube(enhanced_query)
    khan_results = search_khan_academy(enhanced_query)
    combined_results = youtube_results + khan_results

    # Step 4: Store new results in Elasticsearch
    for vid in combined_results:
        store_video(
            video_id=vid["video_id"],
            title=vid["title"],
            description=vid.get("description", ""),
            transcript=vid.get("transcript", ""),  # optional
            source=vid.get("source", "unknown"),
            url=vid.get("url", "")
        )

    print(f"🆕 Stored {len(combined_results)} new results in Elasticsearch")

    return jsonify({
        "videos": combined_results,
        "enhanced_query": enhanced_query
    })

if __name__ == "__main__":
    app.run(debug=True)
