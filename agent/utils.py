import os

from dotenv import load_dotenv
from duckduckgo_search import DDGS
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


def search_web(query):
    results = DDGS().text(query, max_results=5)
    # Convert results to a string
    results_str = "\n\n".join(
        [
            f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}"
            for r in results
        ]
    )
    return results_str
