from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from zai import ZaiClient

app = FastAPI()

load_dotenv()
zai_key = os.getenv('ZAI_API_KEY')
client = ZaiClient(api_key=zai_key)

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=FileResponse)
async def read_root():
        return FileResponse("static/index.html")

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    translated_message: str

class PirateResponse(BaseModel):
    response: str

@app.post("/translate", response_model=MessageResponse)
async def translate_message(request: MessageRequest):
    response = client.chat.completions.create(
        model="glm-4.5-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a translator. You translate input messages into a pirate language. "
                "You try to be concise"
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )
    return MessageResponse(translated_message=response.choices[0].message.content)

@app.post("/pirate-response", response_model=PirateResponse)
async def get_pirate_response(request: MessageRequest):
    response = client.chat.completions.create(
        model="glm-4.5-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a pirate. You response to messages from another pirate."
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )
    return PirateResponse(response=response.choices[0].message.content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)