from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
import crud, schemas
from auth import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# SIGNUP
@router.post("/signup")
async def signup(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(400, "Email already registered")

    await crud.create_user(db, user.email, user.password)
    return {"message": "User created"}

# LOGIN
@router.post("/login")
async def login(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(401, "Invalid email")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(401, "Wrong password")

    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
