import os
from groq import Groq
from twilio.rest import Client
from services.product_service import get_all_products
from services.cart_service import add_to_cart, get_cart

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
twilio_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def send_whatsapp_message(to, text):
    try:
        twilio_client.messages.create(
            from_=os.getenv("TWILIO_NUMBER"),
            body=text,
            to=f"whatsapp:{to}"
        )
    except Exception as e:
        print(f"Twilio Send Error: {e}")

def process_message(sender, user_input):
    user_input = user_input.strip().lower()
    
    # --- 1. THE HARD-CODED MENU LOGIC ---
    # This handles the specific numbers or "hi" triggers without using AI tokens (saving money/speed)
    
    if user_input in ["hi", "hello", "hey", "start"]:
        return (
            "👋 *Welcome to ADA Shop!* \n"
            "How can I help you today? yarr\n\n"
            "1️⃣ *Order:* See our catalog\n"
            "2️⃣ *Review:* Check your shopping cart\n"
            "3️⃣ *Track:* View order status\n"
            "4️⃣ *Special Deals:* Get discounts\n\n"
            "Just type the *number* or tell me what you need!"
        )

    if user_input == "1":
        return (
            "🏷️ *Browse by Category:*\n\n"
            "• *Electronics* (Earbuds, Watches)\n"
            "• *Fashion* (Hoodies, Shoes)\n"
            "• *Home* (Mugs, Lamps)\n\n"
            "Just type a *Category Name* or a specific *Product* to see details!"
        )

    # --- 2. THE AI (GROQ) LOGIC ---
    # If the user types anything else (e.g., "I want a hoodie"), let Groq handle it.
    
    products = get_all_products()
    product_list = "\n".join([f"- {p.name} ({p.category}): ${p.price}" for p in products])
    
    system_prompt = f"""
    You are Ada, a witty Gen-Z shopping assistant. 
    Current Inventory:
    {product_list}

    Instructions:
    - If the user names a category, list products in that category.
    - If the user wants to buy something, confirm and tell them it's added to the cart.
    - Use emojis and keep it brief for WhatsApp.
    """

    completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        model="llama-3.1-8b-instant",
    )
    
    return completion.choices[0].message.content