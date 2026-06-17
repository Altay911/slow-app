from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.database import get_db
from app.models.library import Quote

router = APIRouter(prefix="/quotes", tags=["quotes"])


@router.get("/random")
async def get_random_quote(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Quote).order_by(func.random()).limit(1))
    quote = result.scalar_one_or_none()

    if quote is None:
        raise HTTPException(status_code=404, detail="No quotes found")

    return {
        "id": quote.id,
        "text": quote.text,
        "author_id": quote.author_id,
        "book_id": quote.book_id,
    }