from google import genai
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY_LONGCAT = os.getenv("LONGCAT_API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_code_longCat(chat_id: str, prompt: str, get_latest_version_func) -> str:
    """
    Generates code using LongCat, with previous version context.
    """
    last_version = get_latest_version_func(chat_id)

    if last_version:
        contextual_prompt = f"""
Here is the latest version of the code:

```
{last_version}
```

Now update it based on this request: {prompt}
"""
    else:
        contextual_prompt = prompt

    url = "https://api.longcat.chat/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_LONGCAT}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "LongCat-Flash-Chat",
        "messages": [
            {"role": "user", "content": contextual_prompt}
        ],
        "max_tokens": 8192,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    output = response.json()
    return output["choices"][0]["message"]["content"]

def generate_code(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text
