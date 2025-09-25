from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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