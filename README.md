# Auriel

Backend for condominium delivery management (FastAPI)

## Development database (SQLite)
For quick local development and early testing we use SQLite. The default database URL is set in `.env.example`:

```
DATABASE_URL=sqlite+aiosqlite:///./auriel.db
```

To create the database schema using Alembic:

1. Install dev dependencies: `poetry install`
2. Initialize/upgrade DB: `poetry run alembic upgrade head`

Later we will switch to PostgreSQL with Docker for production and integration testing.