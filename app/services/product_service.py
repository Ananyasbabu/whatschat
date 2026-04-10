import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
BASE_URL = os.getenv("BASE_URL")

client = MongoClient(MONGO_URI)
db = client["shop"]
products_collection = db["products"]

def get_all_products():
    """Fetches all products for the AI to read."""
    products = list(products_collection.find({}))
    formatted_products = []
    
    for p in products:
        formatted_products.append({
            "id": str(p["_id"]),
            "name": p.get("name", "Unknown"),
            "price": f"₹{p.get('price', 0)}"
        })
    return formatted_products

def get_product_by_id(product_id):
    """Fetches a specific product by its MongoDB ObjectID."""
    try:
        p = products_collection.find_one({"_id": ObjectId(product_id)})
        if p:
            # Create a full public URL for Twilio to send the image
            image_path = p.get("imagePath", "")
            full_image_url = f"{BASE_URL}/{image_path}" if image_path else None
            
            return {
                "id": str(p["_id"]),
                "name": p.get("name", "Unknown"),
                "price": f"₹{p.get('price', 0)}",
                "description": p.get("description", ""),
                "image_url": full_image_url
            }
    except Exception as e:
        print(f"Database error: {e}")
    return None