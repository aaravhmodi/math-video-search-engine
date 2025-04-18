print("Script started")

from elasticsearch_utils import store_video, search_elasticsearch, es

print("🚀 Running test script...")

# Step 1: Store a sample video
store_video(
    video_id="sample123",
    title="Intro to Limits - Calculus",
    description="A short video explaining the basic concept of limits in calculus.",
    transcript="A limit describes the behavior of a function as it approaches a particular point.",
    source="YouTube",
    url="https://youtube.com/watch?v=sample123"
)
print("✅ Video stored!")

# Step 2: Refresh the index to make the data searchable
try:
    es.indices.refresh(index="videos")
    print("🔄 Index refreshed!")
except Exception as e:
    print("⚠️ Error refreshing index:", e)

# Step 3: Search for the keyword 'limits'
results = search_elasticsearch("limits")

# Step 4: Check if index exists
if not es.indices.exists(index="videos"):
    print("❌ Index 'videos' does not exist!")
else:
    count = es.count(index="videos")["count"]
    print(f"📊 Index exists. Document count: {count}")

# Step 5: Print the search results
print("🔍 Search results:")
for i, result in enumerate(results, 1):
    print(f"{i}. {result['title']} ({result['url']}) - Score: {result['score']}")
