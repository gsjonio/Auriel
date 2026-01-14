from __future__ import with_statement

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# add project root to path so models can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
try:
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)
except Exception:
    # ignore logging configuration errors in this environment
    pass

# Import metadata from the project
from models.base import Base  # noqa: E402


# If using async DB URLs (sqlite+aiosqlite), Alembic requires a sync URL.
def get_sync_url():
    url = os.getenv("DATABASE_URL", None) or config.get_main_option("sqlalchemy.url")
    if not url:
        return url
    # Handle known async dialect suffixes used by SQLAlchemy async drivers
    for async_suffix in ("+aiosqlite", "+asyncpg"):
        if async_suffix in url:
            return url.replace(async_suffix, "")
    # Fallback: return the URL unchanged if no async suffix detected
    return url


config.set_main_option("sqlalchemy.url", get_sync_url())

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
