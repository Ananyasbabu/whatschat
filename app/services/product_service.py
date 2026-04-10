import os
import json

def get_all_products():
    # This gets the directory of THIS file (the services folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Since products.json is in the SAME folder as this script:
    FILE_PATH = os.path.join(current_dir, "products.json")
    
    if not os.path.exists(FILE_PATH):
        print(f"❌ ERROR: Still can't find it! Looked at: {FILE_PATH}")
        return []
    
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_product_by_id(product_id):
    products = get_all_products()
    for p in products:
        if str(p.get('id', '')).lower() == product_id.lower():
            return p
    return None