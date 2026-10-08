from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/db")
def health_db(db: Annotated[Session, Depends(get_db)]) -> dict[str, str]:
    try:
        version = db.execute(text("SELECT CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(32))"))
        return {"status": "ok", "sql_server": version.scalar_one()}
    except Exception as exc:  # surface DB connectivity problems as 503
        raise HTTPException(status_code=503, detail=f"database unavailable: {exc}") from exc
