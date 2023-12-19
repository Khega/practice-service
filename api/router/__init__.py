from fastapi import APIRouter
from api.src.endpoints import goods

router = APIRouter()

router.include_router(goods.router, prefix="/goods", tags=["goods"])



