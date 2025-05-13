from sqlalchemy.orm import Session
from app import models, schemas

# app/crud.py

def get_items(db: Session, skip: int = 0, limit: int = 1000, room_id: int = None, category_id: int = None):
    query = db.query(models.Item)

    if room_id is not None:
        query = query.filter(models.Item.room_id == room_id)
    if category_id is not None:
        query = query.filter(models.Item.category_id == category_id)

    return query.order_by(models.Item.purchase_date.desc()).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_rooms(db: Session):
    return db.query(models.Room).all()

def get_categories(db: Session):
    return db.query(models.Category).all()

def create_room(db: Session, room: schemas.RoomBase):
    db_room = models.Room(name=room.name)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def create_category(db: Session, category: schemas.CategoryBase):
    db_cat = models.Category(name=category.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat