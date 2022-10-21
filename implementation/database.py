from sqlmodel import Session, create_engine

import settings

engin = create_engine(
    settings.database_url
)


async def get_session():
    '''
    Реализации сессии для работы с базой данных
    :return:
    '''
    with Session(engin) as session:
        yield session
