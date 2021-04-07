from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from sql_app import schemas, crud

router = APIRouter()

@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items