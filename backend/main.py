from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .utils import save_version, get_version, get_latest_version
from .gemini_client import generate_code_longCat  # 👈 use this

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_post(req: Request):
    data = await req.json()
    prompt = data["prompt"]
    chat_id = data.get("chat_id", "default")

    # Pass the helper function
    code = generate_code_longCat(chat_id, prompt, get_latest_version)

    version = save_version(chat_id, code)
    return {"version": version, "code": code}



@app.get("/history/{chat_id}/{version}")
async def get_history(chat_id: str, version: int):
    code = get_version(chat_id, version)
    return {"version": version, "code": code}
