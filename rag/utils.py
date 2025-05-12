import os

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI, api_key

load_dotenv()

base_url = os.environ.get("BASE_URL")
api_key = os.environ.get("API_KEY")
model = os.environ.get("MODEL")

client = OpenAI(api_key=api_key, base_url=base_url)

# print(f"api_key: {api_key}\nbase_url: {base_url}\nmodel: {model}\n")


def call_llm(prompt):
    r = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )

    return r.choices[0].message.content


def get_embedding(text):
    response = client.embeddings.create(model="BAAI/bge-m3", input=text)

    # Extract the embedding vector from the response
    embedding = response.data[0].embedding

    # Convert to numpy array for consistency with other embedding functions
    return np.array(embedding, dtype=np.float32)


def fixed_size_chunk(text, chunk_size=2000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks
