from pydantic import BaseModel
from typing import Optional
from datetime import date

# Room schema
class RoomBase(BaseModel):
    name: str

class Room(RoomBase):
    room_id: int
    class Config:
        orm_mode = True

# Category schema
class CategoryBase(BaseModel):
    name: str

class Category(CategoryBase):
    category_id: int
    class Config:
        orm_mode = True

# Item schema
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = 1
    purchase_date: Optional[date] = None
    room_id: int
    category_id: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    item_id: int
    class Config:
        orm_mode = True