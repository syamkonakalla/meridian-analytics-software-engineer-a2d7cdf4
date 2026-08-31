# Meridian Analytics — Software Engineer Workspace

> **CareerSim workspace** | TestUser | Software Engineer

## About Meridian Analytics
Meridian processes event streams from 300+ enterprise clients, turning raw behavioural data into actionable insights. The platform handles ~4 billion events/day across retail, fintech, and logistics verticals.

## Current Sprint
**Customer churn prediction pipeline (ML-powered, Sprint 14)**

The churn model needs to be live by end of quarter — three enterprise clients are threatening to churn themselves if we can't show them predictive retention insights.

## Project State
**What's built:** Bronze ingestion layer is stable and handles raw event streams. Silver transformation cleans and validates ~95% of data. A basic reporting dashboard is live for 12 clients.

**In progress:** The Gold aggregation layer is half-done — feature engineering for churn scoring is blocked on schema decisions. Python jobs are flaky on weekends due to a known memory leak.

**Known issues:** 1) Bronze→Silver schema drift breaks downstream jobs 2-3x/week with no alerting. 2) No CI for pipeline code — everything goes straight to prod.

## Your Mission
Own the Silver→Gold pipeline: implement churn feature engineering using Python, resolve the weekend memory leak, and get the ML team unblocked.

## Team
| Name | Role |
|------|------|
| Alex Mercer | Engineering Manager |
| Rohan Verma | Lead Software Engineer |
| Emily Chen  | Data Analyst |
| David Park  | DevOps |
| **TestUser** | **Software Engineer (You — inheriting from previous engineer)** |

## Tech Stack
- Python
- FastAPI

## Workflow
1. Check email for Jira ticket notifications
2. Create branch: `git checkout -b TASK-XXX/short-description`
3. Push code → open PR → tag Alex for review
4. Daily standup at 10am in CareerSim chat

---
*CareerSim workspace · GitHub Issues = your Jira board*
