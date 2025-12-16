from fastapi import FastAPI, HTTPException
from src import types
from src.chat import suscribe, post_message
import uvicorn

app = FastAPI()


# @app.post("/suscribe", response_model=types.SuscribeOutputModel, response_model_by_alias=True)
# async def suscribe(request: types.SuscribeInputModel):
#     try:
#         answ = suscribe(request)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
#     return answ

@app.post("/post_message", response_model=types.ChatModel, response_model_by_alias=True)
async def post_message(message: types.MessageModel):
    try:
        answ = post_message(message) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return answ

@app.get("/health")
async def health_check() -> str:
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)