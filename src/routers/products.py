"""
Products router

TODO (TASK-101): Add POST /products endpoint with owner validation.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src import models

router = APIRouter(prefix='/products', tags=['products'])


@router.get('/')
def list_products(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.is_active == True).offset(skip).limit(limit).all()


@router.get('/{product_id}')
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    return p


# TODO (TASK-101): implement POST /products
# Required fields: name, description, price_cents, owner_id
# Validate owner exists before creating product
# Return 201 Created with the new product object
