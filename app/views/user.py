from typing import List
from logs import logger
from shema import UsersShem
from fastapi import APIRouter
from database.database import users, database

# Вызов роутеров для пользователей
users_router = APIRouter()

# CRUD реализован согласно тз все запросы строятся примерно 
# по одному и томуже шаблону :
# @метод_запроса("URL-rout", модель_ответа) 
# объявление запроса к бд (чтени, удаление и т.д.) 
# создание записи логером 
# return...

# Создание Users
@users_router.put("/users/", response_model=UsersShem)
async def create_user(user: UsersShem) -> UsersShem:
    query = users.insert().values(
        full_name=user.full_name,
        gender=user.gender,
        birth_day=user.birth_day,
        address=user.address
    )
    logger.warning("user create")
    user.id = await database.execute(query)
    return user


# Чтение всех Users
@users_router.post('/users/', response_model=List[UsersShem])
async def read_all_user() -> List[UsersShem]:
    query = users.select()
    return await database.fetch_all(query)


# Чтение Users по id
@users_router.post('/users/{users_id}/', response_model=UsersShem)
async def read_user_on_id(_id: int) -> UsersShem:
    query = users.select().where(users.c.id == _id)
    return await database.fetch_one(query)


# Изменение  Users
@users_router.patch('/users/', response_model=UsersShem)
async def update_user(user: UsersShem, _id: int) -> UsersShem:
    query = users.update().where(users.c.id == _id).values(
        full_name=user.full_name,
        gender=user.gender,
        birth_day=user.birth_day,
        address=user.address
    )
    logger.warning(f"user update")
    await database.execute(query)
    return user


# Удаление Users
@users_router.delete('/users/', response_model=UsersShem)
async def delete_user(_id: int):
    query = users.delete().where(users.c.id == _id)
    logger.warning("user delete")
    return await database.execute(query)
