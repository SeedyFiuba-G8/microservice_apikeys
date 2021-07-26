from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers import routers_list
from src.config import config


app = FastAPI(**config.OPENAPI_SETTINGS)
for router in routers_list:
    app.include_router(router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    '''
    Redirect to '/docs'.
    '''
    return RedirectResponse(url='/docs')
