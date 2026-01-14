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

## Using Poetry (recommended)

- Install Poetry (recommended via pipx):
  - `python -m pip install --user pipx`
  - `python -m pipx ensurepath`
  - `pipx install poetry`

- Ensure project uses Python 3.11. If needed, point Poetry to your Python 3.11 executable:
  - `poetry env use C:\\path\\to\\python3.11.exe`

- Install dependencies (without installing the package root):
  - `poetry install --no-root`

- Run tests:
  - `poetry run pytest -q`

Notes:
- If `poetry install` complains about the lockfile, run `poetry lock` and try again.
- For CI, set the runner Python to `3.11` and run `poetry install --no-root` followed by `poetry run pytest -q`.