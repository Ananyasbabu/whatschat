# Simple storage: { "phone_number": [product_ids] }
user_carts = {}

def add_to_cart(user_id, product_id):
    if user_id not in user_carts:
        user_carts[user_id] = []
    user_carts[user_id].append(product_id)

def get_cart(user_id):
    from services.product_service import inventory
    product_ids = user_carts.get(user_id, [])
    # Return actual product objects found in inventory
    return [p for p in inventory if p.id in product_ids]