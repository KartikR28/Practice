from fastapi import FastAPI
from database import engine, Base
from routers import auth_router, item_router

app = FastAPI(title="JWT Auth CRUD API")

app.include_router(auth_router.router)
app.include_router(item_router.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def home():
    return {"message": "Running"}
