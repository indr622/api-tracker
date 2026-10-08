# api-tracker

API Task Tracker (FastAPI, SQLAlchemy, Celery, uv).

## Setup
- `.env`: `DATABASE_URL=postgresql+psycopg://user:pass@localhost:5433/db_tracker`
- `uv sync && uv run alembic upgrade head`
- `uv run api-tracker`

## Git workflow
Semantic commit (`chore`, `feature`, `bugfix`, `fix`) divalidasi hook di `scripts/hooks`
(aktifkan: `git config core.hooksPath scripts/hooks`).
Auto commit & push: `scripts/commit.sh feature "pesan"`.
