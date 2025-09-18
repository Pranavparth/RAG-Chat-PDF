from transformers import pipeline

# Free HuggingFace LLM
generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

def generate_answer(query, context):
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    response = generator(prompt, max_new_tokens=200)[0]["generated_text"]
    return response
