from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("HF TOKEN FOUND:", hf_token is not None)
print("HF TOKEN PREVIEW:", hf_token[:6] if hf_token else "None")
