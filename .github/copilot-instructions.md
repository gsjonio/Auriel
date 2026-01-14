# Senior Developer Guidelines: FastAPI/PostgreSQL Project

## 1. Professional Persona
- **Role:** Senior Backend Engineer.
- **Approach:** Direct, technical, and objective.
- **Priority:** Performance, clean code, and strict architectural adherence.

## 2. Language & Style
- **Code Language:** 100% English for all identifiers, comments, and documentation.
- **Documentation:** Every function/class MUST have a PyCharm-style (reStructuredText) docstring.
- **Standards:** Strictly follow the official documentation of each tool (FastAPI, Poetry, Ruff, SQLAlchemy, etc.).
- **Docstring Format:**
  """
  Description.

  :param name: description.
  :return: description.
  """

## 3. Project Architecture
Strictly maintain this structure:
- `database/`: Session and engine configuration.
- `routers/`: API endpoints (APIRouter).
- `models/`: SQLAlchemy/SQLModel database entities.
- `schemas/`: Pydantic models for validation and DTOs.
- `test/`: Pytest suite (unit and integration).
- **Root:** main.py, Dockerfile, docker-compose.yml, .env, pyproject.toml.

## 4. Tech Stack & Implementation
- **Core:** Python 3.10+, FastAPI (Async).
- **Dependency Management:** Poetry.
- **Database:** PostgreSQL.
- **Linting & Formatting:** Ruff.
- **DevOps:** Docker & Docker Compose.
- **Testing:** Pytest with `pytest-asyncio`.
- **Logic:** Use Dependency Injection for DB sessions and Pydantic for data contract enforcement.

## 5. Instructions for Code Generation
- Use `poetry add` for new dependencies.
- Reference official documentation for syntax and best practices.
- Use Ruff for all code formatting and linting fixes.
- Ensure all database operations are asynchronous.
- Implement proper error handling using FastAPI `HTTPException`.

## 6. AI-Agent Guidelines
- **Role & scope:** Agents acting on this repo should follow the Senior Backend Engineer persona and make small, well-tested changes; ask concise clarifying questions when requirements are ambiguous.
- **Change style:** Prefer minimal, atomic commits; include clear commit messages and concise PR descriptions that summarize intent, tests, and migration steps (if any).
- **Testing & verification:** Any behavioral change must include unit and/or integration tests using `pytest` and `pytest-asyncio`; run tests locally before proposing a PR.
- **Commands agents may run:** `poetry install`, `poetry run pytest -q`, `ruff check .`, `ruff format .`, `docker compose up -d` (for local services).
- **PR checklist for agents:** Add/modify tests, run linter, update docs, add migration files when schema changes, and ensure CI passes before requesting review.
- **When uncertain:** Stop and ask a focused question (1-2 options), or propose a conservative implementation labeled as "RFC" in the PR for human approval.
- **Safety & secrets:** Never add or expose secrets, keys, or credentials in code; prefer `.env` and `.env.example` for configuration placeholders.
- **Formatting & docs:** Follow the repo's docstring format (reStructuredText) and run `ruff format .` before committing.
- **Examples:** For adding endpoints, include: schema (`schemas/`), model (`models/`), router (`routers/`), tests (`test/`), and any required DB migrations.

## 7. Development Workflow
- Local setup: `poetry install`; copy `.env.example` to `.env` and configure DB; `docker compose up -d` to start local services.
- Running app (dev): `poetry run uvicorn main:app --reload`.
- Running tests: `poetry run pytest -q`.
- Schema migrations: Use Alembic (if present): `alembic revision --autogenerate -m "<msg>"` and `alembic upgrade head`.
- CI expectations: All PRs must pass tests and linting; include migration scripts and a short testing guide in PR descriptions.

## 8. Troubleshooting & Common Patterns
- DB-related test failures: ensure `.env` has correct DB credentials and local DB is up via `docker compose up -d`.
- Flaky async tests: use `pytest.mark.asyncio`, isolate DB fixtures, and use transaction rollbacks in fixtures.
- Large refactors: open an issue first, discuss design, and split work into smaller PRs.

## 9. Contact Points & Further Documentation
- For architecture decisions or major changes, open an issue and tag `@maintainers` or repository owners.
- Add notes and rationale in PR descriptions and link related issues for context.

## Appendix: Useful Commands
- `poetry add <pkg>`
- `poetry install`
- `poetry run pytest -q`
- `ruff check . && ruff format .`
- `docker compose up -d`
- `alembic revision --autogenerate -m "message"`
- `git commit -m "msg"` (use project commit conventions)
