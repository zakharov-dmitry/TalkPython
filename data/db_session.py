from typing import Optional, Callable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import settings
from data.modelbase import SqlAlchemyBase

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
__factory: Optional[Callable[[], Session]] = None


def global_init():
    global __factory
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
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


