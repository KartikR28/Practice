from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import crud, schemas
from dependencies import get_current_user

router = APIRouter(prefix="/items", tags=["Items"])

# CREATE (Protected)
@router.post("/")
async def create_item(
    item: schemas.ItemCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await crud.create_item(db, item)

# READ
@router.get("/")
async def read_items(
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await crud.get_items(db)

# DELETE
@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await crud.delete_item(db, item_id)
