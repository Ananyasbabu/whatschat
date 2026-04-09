import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
# IMPORTANT: Since you are running FROM the app folder, 
# use 'from routes.webhook' instead of 'from app.routes.webhook'
from routes.webhook import router as webhook_router 

app = FastAPI()

# Use the name you defined in the import above
app.include_router(webhook_router)

@app.get("/")
def home():
    return {"message": "E-commerce Chatbot Running 🚀"}