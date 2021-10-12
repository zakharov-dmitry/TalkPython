import fastapi

router = fastapi.APIRouter()


@router.get('/')
def index():
    content = """
    <h1>Hello world</h1>
    <div>This is where our fake pipy will live!</div>
    """
    return fastapi.responses.HTMLResponse(content)


@router.get('/about')
def index():
    return {}
