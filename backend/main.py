#uvicorn main:app
#uvicorn main:app --reload
#Main import 
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai 

#custom function imports


#Initiate App
app = FastAPI()

#CORS  - Origins


@app.get("/")
async def root():
    return {"message": "Hello alls"}