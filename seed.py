from app import models
from app.database import engine, SessionLocal
from datetime import date
import random

# Setup session
db = SessionLocal()

# Existing room and category IDs
room_ids = [1, 2, 3, 4]  # Living Room, Kitchen, Bedroom, Garage
category_ids = [1, 2, 3, 4]  # Furniture, Electronics, Kitchenware, Clothing

sample_items = [
    "Chair", "Lamp", "TV", "Coffee Table", "Bookshelf", "Fan", "Air Conditioner",
    "Fridge", "Toaster", "Blender", "Dish Rack", "Pan", "Pot", "Knife Set", "Cutting Board",
    "T-Shirt", "Jeans", "Jacket", "Sweater", "Shoes", "Slippers", "Laundry Basket",
    "Drill", "Screwdriver", "Hammer", "Saw", "Wrench", "Toolbox", "Extension Cord",
    "Wall Clock", "Painting", "Curtains", "Desk", "Monitor", "Keyboard", "Mouse",
    "Printer", "Router", "Speaker", "Remote", "Game Console", "Notebook", "Pencil Case",
    "Iron", "Mop", "Vacuum", "Broom", "Trash Can", "Recycle Bin", "Water Bottle"
]

# Shuffle to ensure variety
random.shuffle(sample_items)

for i, name in enumerate(sample_items[:50]):
    item = models.Item(
        name=name,
        description=f"{name} used around the house",
        quantity=random.randint(1, 5),
        purchase_date=date(2022 + (i % 3), random.randint(1, 12), random.randint(1, 28)),
        room_id=random.choice(room_ids),
        category_id=random.choice(category_ids)
    )
    db.add(item)

db.commit()
db.close()
print("✅ 50 sample items added successfully.")