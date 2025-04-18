from dotenv import load_dotenv
import os
import requests

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = "t5-small"

def enhance_query(query):
    try:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {
            "inputs": f"paraphrase: {query} </s>"
        }

        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            enhanced = data[0]["generated_text"]
            print(f"🔁 Query enhanced: {query} → {enhanced}")
            return enhanced.strip()
        else:
            print("⚠️ Unexpected response format from Hugging Face:", data)
            return query

    except requests.exceptions.RequestException as e:
        print("❌ Hugging Face API error:", e)
        return query
