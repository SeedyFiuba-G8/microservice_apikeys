from .keys import router as keys_router
from .status import router as status_router

routers_list: list = [
    keys_router,
    status_router
]
