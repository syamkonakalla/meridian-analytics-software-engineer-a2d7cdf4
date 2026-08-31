# Onboarding — TestUser | Software Engineer
**Company:** Meridian Analytics | **Manager:** Alex Mercer

Welcome. This doc covers what you need to know in your first week.

## The Product
Meridian processes event streams from 300+ enterprise clients, turning raw behavioural data into actionable insights. The platform handles ~4 billion events/day across retail, fintech, and logistics verticals.

We're currently in **Sprint Customer churn prediction pipeline (ML-powered, Sprint 14)**. The churn model needs to be live by end of quarter — three enterprise clients are threatening to churn themselves if we can't show them predictive retention insights.

## The Team
| Name | Role | Contact |
|------|------|--------|
| Alex Mercer | Engineering Manager | Slack: @alex |
| Rohan Verma | Senior Software Engineer | Slack: @rohan — owns core API + DB schema |
| Emily Chen | Product / QA | Slack: @emily — owns acceptance criteria |
| David Park | DevOps / Infra | Slack: @david — CI/CD, Postgres, Redis |
| **TestUser** | **Software Engineer** | **That's you** |

## Architecture
```
Client (browser/mobile)
    ↓ HTTPS
FastAPI app (src/main.py)
    ↓ SQLAlchemy ORM
Postgres (prod) / SQLite (local dev)
    ↓
Alembic migrations (alembic/)
```

## What's Built vs. What's Missing
**Working:**
- GET /api/v1/users/ and /api/v1/products/ (read-only)
- Health check endpoint
- SQLite local dev setup

**Your sprint work:**
The Gold aggregation layer is half-done — feature engineering for churn scoring is blocked on schema decisions. Python jobs are flaky on weekends due to a known memory leak.

**Known issues:**
1) Bronze→Silver schema drift breaks downstream jobs 2-3x/week with no alerting. 2) No CI for pipeline code — everything goes straight to prod.

## Environment Setup
1. Clone repo and install deps: `pip install -r requirements.txt`
2. Run dev server: `uvicorn src.main:app --reload`
3. Swagger UI: http://localhost:8000/docs
4. Run tests: `pytest tests/ -v`
5. Ask David for Postgres connection string if you need staging access

## Git Workflow
```bash
git checkout -b TASK-XXX/short-description
# ... make changes ...
git commit -m "feat(users): add POST /users endpoint (TASK-101)"
git push origin TASK-XXX/short-description
# Open PR — tag Alex for review
```
