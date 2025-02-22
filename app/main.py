from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.faiss_index import FaissIndex
from app.llm import *

app = FastAPI()
bd = FaissIndex(5)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

class MessageRequest(BaseModel):
    text: str

@app.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@app.post("/api/send-message")
async def sendMessage(request: MessageRequest):
    user_input = request.text
    #bd.add_vectors(get_emotions(user_input))
    print(get_emotions(user_input))
    return {"result": chat(user_input)}





