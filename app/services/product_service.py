class Product:
    def __init__(self, id, name, category, price, description, image_url):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.image_url = image_url

# Synthetic Demo Dataset
inventory = [
    # Electronics
    Product(1, "Wireless Earbuds", "Electronics", 50, "Crystal clear sound with 24h battery.", "https://example.com/buds.jpg"),
    Product(2, "Smart Watch", "Electronics", 120, "Track your fitness and heart rate.", "https://example.com/watch.jpg"),
    Product(3, "Power Bank", "Electronics", 30, "20,000mAh fast-charging power bank.", "https://example.com/power.jpg"),
    
    # Fashion
    Product(4, "Oversized Hoodie", "Fashion", 45, "Premium cotton, perfect for techies.", "https://example.com/hoodie.jpg"),
    Product(5, "Running Shoes", "Fashion", 80, "Lightweight shoes for daily marathons.", "https://example.com/shoes.jpg"),
    
    # Home & Living
    Product(6, "LED Desk Lamp", "Home", 25, "Adjustable brightness for late-night coding.", "https://example.com/lamp.jpg"),
    Product(7, "Ceramic Coffee Mug", "Home", 15, "Minimally designed for your desk.", "https://example.com/mug.jpg")
]

def get_products_by_category(category):
    return [p for p in inventory if p.category.lower() == category.lower()]

def get_all_products():
    return inventory