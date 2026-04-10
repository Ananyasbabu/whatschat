from fastapi import APIRouter, Form
from services.ai_service import process_message, send_whatsapp_message

router = APIRouter()

@router.post("/webhook")
async def webhook(
    From: str = Form(...), 
    Body: str = Form(...)
):
    """
    Handles incoming WhatsApp/Instagram messages from Twilio.
    """
    try:
        # 1. Clean the sender number (Important for the session key)
        # Twilio sends 'whatsapp:+123456789' or 'messenger:12345'
        sender_id = From.replace("whatsapp:", "").replace("messenger:", "")
        message_body = Body

        # 2. Get the response from AI service
        # result = {"text": "...", "image": "..."}
        result = process_message(sender_id, message_body)

        # 3. Send the message back
        send_whatsapp_message(
            to=sender_id, 
            text=result.get('text', "Sorry, I encountered an error. yarr"), 
            image_url=result.get('image')
        )

        # 4. Debugging (Helps you see if 'Buy' is working during the demo)
        print(f"📩 Incoming from {sender_id}: {message_body}")
        if message_body.lower() == "buy":
            print(f"💰 BUY TRIGGERED for {sender_id}")

        return {"status": "success"}

    except Exception as e:
        print(f"❌ Webhook Error: {e}")
        return {"status": "error", "message": str(e)}