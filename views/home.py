import fastapi
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = fastapi.APIRouter()


templates = Jinja2Templates("templates")

@router.get('/')
def index(request : Request, user : str = 'anon'):
    content = {"user_name":"new_user"}
    return templates.TemplateResponse("home/index.j2", {'request': request, 'user_name' : user})


@router.get('/about')
def index():
    return {}
