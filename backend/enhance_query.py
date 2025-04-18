from sentence_transformers import SentenceTransformer, util

# Load a lightweight model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Some manually curated common math-related paraphrases
query_templates = [
    "Explain {}",
    "What is {}?",
    "Introduction to {}",
    "Understanding {}",
    "Overview of {}",
    "Basic concept of {}",
    "Definition of {}",
    "{} tutorial"
]

def enhance_query(query, top_k=1):
    candidates = [template.format(query) for template in query_templates]
    query_embedding = model.encode(query, convert_to_tensor=True)
    candidate_embeddings = model.encode(candidates, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(query_embedding, candidate_embeddings)[0]
    top_results = similarities.topk(k=top_k)

    enhanced = candidates[top_results[1][0].item()]
    print(f"🔁 Query enhanced: {query} → {enhanced}")
    return enhanced
