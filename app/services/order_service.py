orders = []

def create_order(session):
    order = {
        "items": session["cart"],
        "status": "placed"
    }
    orders.append(order)
    session["cart"] = {}
    return "Order placed successfully 🎉"