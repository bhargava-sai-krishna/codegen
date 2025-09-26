import requests

url = "https://api.longcat.chat/openai/v1/chat/completions"
headers = {
    "Authorization": "Bearer ak_1E712f7op03g5HD2nO4ze7g549Q2Q",
    "Content-Type": "application/json"
}

data = {
    "model": "LongCat-Flash-Chat",
    "messages": [
        {"role": "user", "content": "Hello, please introduce yourself."}
    ],
    "max_tokens": 1000,
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
