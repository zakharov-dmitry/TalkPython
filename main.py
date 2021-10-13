import fastapi
import uvicorn
from views import home
from views import account
from views import packages
import fastapi_chameleon

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)

def configure():
    configure_routes()
    configure_templates()

def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def configure_templates():
    fastapi_chameleon.global_init('templates')


if __name__ == '__main__':
    main()
else:
    configure()
