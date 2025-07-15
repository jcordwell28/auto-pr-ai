from dotenv import load_dotenv
import os

load_dotenv()

print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))
print("GitHub Token:", os.getenv("GITHUB_TOKEN"))