from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

class MessageRequest(BaseModel):
    text: str

@app.get("/")
async def read_index():
    return FileResponse("app/static/index.html")

@app.post("/api/send-message")
async def sendMessage(request: MessageRequest):
    return {"result": request.text}





