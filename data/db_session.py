from typing import Optional, Callable
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from config import settings
from data.modelbase import SqlAlchemyBase

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
ASYNC_SQLALCHEMY_DATABASE_URL = settings.ASYNC_POSTGRES_URL
__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None


def global_init():
    global __factory, __async_engine
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    __async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
    __factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    import data.__all_models
    SqlAlchemyBase.metadata.create_all(bind=engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method.")

    session: Session = __factory()
    session.expire_on_commit = False

    return session

def create_async_session() -> AsyncSession:
    global __async_engine
    if not __async_engine:
        raise Exception("You must call global_init() before using this method.")
    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False
    return session


