from fastapi import APIRouter

from .operationuser import routerUser

router = APIRouter
router.include_router(routerUser)