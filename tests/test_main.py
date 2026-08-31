"""
API Tests — Meridian Analytics
Run: pytest tests/ -v --cov=src

NOTE: Uses SQLite in-memory for isolation. Each test gets a fresh DB.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database import Base, get_db


@pytest.fixture(scope='function')
def test_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestingSession()
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(test_db):
    return TestClient(app)


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_list_users_empty(client):
    r = client.get("/api/v1/users/")
    assert r.status_code == 200
    assert r.json() == []


def test_get_nonexistent_user(client):
    r = client.get("/api/v1/users/999")
    assert r.status_code == 404


# TODO (TASK-101): Add test for POST /api/v1/products once endpoint is implemented
# TODO (TASK-102): Add test that verifies search uses index (check EXPLAIN output)
