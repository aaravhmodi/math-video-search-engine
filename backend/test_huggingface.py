from huggingface_utils import enhance_query

print("🔍 Testing Hugging Face query enhancement...\n")
original_query = "what is a limit in calculus"
enhanced = enhance_query(original_query)

print(f"\n🔁 Original: {original_query}")
print(f"✨ Enhanced: {enhanced}")
