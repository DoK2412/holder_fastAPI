from fastapi import FastAPI

from .modelsuser import routerUser

app = FastAPI()
app.include_router(routerUser)