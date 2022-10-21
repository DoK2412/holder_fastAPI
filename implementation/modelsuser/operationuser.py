from fastapi import APIRouter


routerUser = APIRouter(
    prefix='/modelsuser'
)

@routerUser.get('/authorization')
async  def authorizationuser():
    return 'ok'