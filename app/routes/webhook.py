from fastapi import APIRouter, Form
from services.ai_service import process_message, send_whatsapp_message # Import the sender

router = APIRouter()

@router.post("/webhook")
async def webhook(
    From: str = Form(...), 
    Body: str = Form(...)
):
    try:
        sender_number = From.replace("whatsapp:", "")
        message_body = Body

        # 1. Generate the reply text using Groq/Logic
        reply = process_message(sender_number, message_body)

        # 2. ACTUALLY SEND THE MESSAGE TO WHATSAPP
        send_whatsapp_message(sender_number, reply)

        # Log to console
        print(f"Incoming from {sender_number}: {message_body}")
        print(f"Reply sent to WhatsApp: {reply}")

        return {"status": "success"}

    except Exception as e:
        print(f"Webhook Error: {e}")
        return {"error": str(e)}