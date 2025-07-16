import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# prompt template
def review_diff(filename, patch, model="gpt-4"):
    messages = [
        {"role": "system", "content": "You are a senior software engineer doing code review. Be constructive, specific, and concise."},
        {"role": "user", "content": f"Please review the following diff in {filename}:\n\n{patch}"}
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
        max_tokens=300 # lower
    )

    return response.choices[0].message.content.strip() # returns Python object not a dictionary