from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database
from fastapi import HTTPException
from app.models import Item

router = APIRouter(prefix="/items", tags=["items"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app/routers/items.py

@router.get("/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    room_id: int = None,
    category_id: int = None,
    search: str = "",
    db: Session = Depends(get_db)
):
    query = db.query(Item)

    if room_id:
        query = query.filter(Item.room_id == room_id)
    if category_id:
        query = query.filter(Item.category_id == category_id)
    if search:
        query = query.filter(Item.name.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()
@router.post("/", response_model=schemas.Item)
def create_new_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}