"""
Meridian Analytics API — Software Engineer Workspace
Owner: TestUser

Current sprint: Customer churn prediction pipeline (ML-powered, Sprint 14)

KNOWN ISSUE: /api/v1/users/search is N+1 querying — TASK-102.
Rohan flagged it in code review last sprint. Do NOT add more callers until fixed.
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import os

from src.database import engine, Base
from src.routers import users, products


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Meridian Analytics API",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock to frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


# TODO (TASK-101): Add rate limiting middleware — David has the Redis config
# TODO (TASK-102): Fix N+1 in /api/v1/users/search — use joinedload or subquery
# TODO (TASK-103): Add request ID middleware for distributed tracing
