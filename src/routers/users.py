"""
Users router

KNOWN ISSUE (TASK-102): GET /users/search does a full table scan with N+1.
Rohan flagged in Sprint 12 PR review. Fix before adding pagination.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.database import get_db
from src import models

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()


@router.get('/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


# TODO (TASK-102): rewrite search to use the composite index (ix_products_owner_active)
# and eliminate N+1. Rohan's suggestion: use joinedload() on the query.
@router.get('/search')
def search_users(q: str = Query(..., min_length=2), db: Session = Depends(get_db)):
    # WARNING: this is doing a LIKE scan on the full table — TASK-102
    return db.query(models.User).filter(models.User.name.ilike(f'%{q}%')).all()
