from pydantic import BaseModel, EmailStr

# ---------- USER ----------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# ---------- ITEM ----------
class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True
