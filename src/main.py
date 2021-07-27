from fastapi import FastAPI, status, Request
from fastapi.responses import RedirectResponse, JSONResponse

from src.assets.responses import Error
from src.exception import APIKeysException
from src.routers import routers_list
from src.config import config

app = FastAPI(
    docs_url='/api-docs',
    **config.OPENAPI_SETTINGS
)


for router in routers_list:
    app.include_router(router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    '''
    Redirect to '/docs'.
    '''
    return RedirectResponse(url='/api-docs')


@app.exception_handler(APIKeysException)
async def apikeys_exception_handler(_: Request, error: APIKeysException):
    return JSONResponse(status_code=error.error.status, content=error.error.dict())


@app.exception_handler(Exception)
async def exception_handler(_: Request, e: Exception):
    print(e)
    error = Error(status=status.HTTP_404_NOT_FOUND, name='Not found.')
    return JSONResponse(status_code=error.status,
                        content=error.dict())
