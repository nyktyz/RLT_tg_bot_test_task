from logging.config import fileConfig

import sys
import importlib
from importlib import util
from pathlib import Path

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

p = Path(__file__).parents[1] / "src"

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

database = importlib.import_module("rlt_tg_bot_test_task.database", str(p))
importlib.import_module("rlt_tg_bot_test_task.models", str(p))
target_metadata = database.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

settings = importlib.import_module("rlt_tg_bot_test_task.config", str(p)).settings
database_url = settings.database_settings.database_url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = database_url
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    conf = config.get_section(config.config_ini_section, {})
    conf.update({
        "sqlalchemy.url": database_url
    })

    connectable = engine_from_config(
        conf,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


# p = Path(__file__).parents[1]
# p = Path(__file__).parents[1] / "src" / "rlt_tg_bot_test_task" / "config.py"
# p = Path(__file__).parents[1] / "src" / "rlt_tg_bot_test_task"
# p = "config.py"
# print(importlib.import_module("config.py", package=str(p)))
# print(importlib.import_module(".src.rlt_tg_bot_test_task.config.py", package=str(p)))
print()