"""
SQLAlchemy ORM Models — Meridian Analytics

CAUTION: Use Alembic for schema changes, NOT Base.metadata.create_all() in prod.
David has alembic configured in alembic/. Never edit migration files by hand.
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    email      = Column(String, unique=True, nullable=False, index=True)
    name       = Column(String, nullable=False)
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # TODO (TASK-101): Add role field (admin/viewer/editor) for RBAC


class Product(Base):
    __tablename__ = "products"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    description = Column(String)
    price_cents = Column(Integer, nullable=False)  # store in cents, display in dollars
    is_active   = Column(Boolean, default=True)
    owner_id    = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at  = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    owner = relationship('User', back_populates='products')

    # Composite index for the search query Rohan complained about (TASK-102)
    __table_args__ = (
        Index('ix_products_owner_active', 'owner_id', 'is_active'),
    )
