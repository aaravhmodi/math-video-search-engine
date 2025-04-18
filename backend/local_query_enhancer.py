from sentence_transformers import SentenceTransformer, util

# Load a lightweight, performant model
model = SentenceTransformer("all-MiniLM-L6-v2")

def enhance_query_local(query, related_texts):
    """
    Enhance a query by selecting the most semantically similar phrase
    from a predefined list (or previous queries, or document titles, etc.)
    """
    # Embed the query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Embed related texts (e.g., predefined set of math phrases)
    corpus_embeddings = model.encode(related_texts, convert_to_tensor=True)

    # Compute cosine similarity
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1)[0]
    best_match = related_texts[hits[0]['corpus_id']]

    print(f"🔁 Original: {query}")
    print(f"✨ Enhanced: {best_match}")
    return best_match
