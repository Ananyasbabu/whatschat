import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.webhook import router as webhook_router 

app = FastAPI()

# This line makes your images publicly accessible!
app.mount("/img", StaticFiles(directory="img"), name="img")

app.include_router(webhook_router)

@app.get("/")
def home():
    return {"message": "E-commerce Chatbot Running 🚀"}