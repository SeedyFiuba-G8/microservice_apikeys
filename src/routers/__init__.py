from src.routers.keys import router as keys_router
from src.routers.status import router as status_router
from src.routers.auth import router as auth_router

routers_list: list = [
    keys_router,
    status_router,
    auth_router
]
