from fastapi import FastAPI
from app.routers import quotes

app = FastAPI(title="slow.")

app.include_router(quotes.router)


@app.get("/")
async def root():
    return {"message": "slow."}