# app/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity = Column(Integer, default=1)
    purchase_date = Column(Date)
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    category_id = Column(Integer, ForeignKey("categories.category_id"))

    room = relationship("Room")
    category = relationship("Category")