from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

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
    return MessageResponse(translated_message=request.message)

@app.post("/pirate-response", response_model=PirateResponse)
async def get_pirate_response(request: MessageRequest):
    return PirateResponse(response="Arrr, matey! That be a fine question indeed!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)