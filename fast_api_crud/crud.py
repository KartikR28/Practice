from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Item

# CREATE
async def create_item(db: AsyncSession, item):
    new_item = Item(**item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

# READ ALL
async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Item
from auth import hash_password

# -------- USER ----------
async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()

# -------- ITEM ----------
async def create_item(db: AsyncSession, item):
    new_item = Item(**item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

async def get_items(db: AsyncSession):
    result = await db.execute(select(Item))
    return result.scalars().all()

async def delete_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()

    if not item:
        return None

    await db.delete(item)
    await db.commit()
    return {"message": "Deleted"}

# READ ONE
async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()

# UPDATE
async def update_item(db: AsyncSession, item_id: int, item_data):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()

    if not item:
        return None

    item.name = item_data.name
    item.description = item_data.description
    item.price = item_data.price

    await db.commit()
    await db.refresh(item)
    return item

# DELETE
async def delete_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()

    if not item:
        return None

    await db.delete(item)
    await db.commit()
    return item
