import fastapi
import uvicorn

from data import db_session
from views import home
from views import account
from views import packages
import fastapi_chameleon
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)


def configure():
    configure_routes()
    configure_templates()
    configure_db()


def configure_db():
    db_session.global_init()


def configure_routes():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def configure_templates():
    fastapi_chameleon.global_init('templates')


if __name__ == '__main__':
    main()
else:
    configure()
