from typing import List
from logs import logger
from shema import PhonesShem
from fastapi import APIRouter
from database.database import phones, database

# Вызов роутеров для телефонов
phone_router = APIRouter()


# Создание Phones
@phone_router.put("/phones/", response_model=PhonesShem)
async def create_phone(phone: PhonesShem):
    query = phones.insert().values(
        type_phone=phone.type_phone,
        number_phone=phone.number_phone,
        user_id=phone.user_id
    )
    logger.warning("phone create")
    phone.id = await database.execute(query)
    return phone


# Чтение всех Phones
@phone_router.post('/phone/', response_model=List[PhonesShem])
async def read_all_phone():
    query = phones.select()
    return await database.fetch_all(query)


# Чтение Phones по id
@phone_router.post('/phone/{phones_id}/', response_model=PhonesShem)
async def read_phone(_id: int):
    query = phones.select().where(phones.c.id == _id)
    return await database.fetch_one(query)


# Изменение Phones
@phone_router.patch('/phone/', response_model=PhonesShem)
async def update_phone(phone: PhonesShem, _id: int):
    query = phones.update().where(phones.c.id == _id).values(
        type_phone=phone.type_phone,
        number_phone=phone.number_phone
    )
    logger.warning("phone update")
    await database.execute(query)
    return phone


# Удаление Phones
@phone_router.delete('/phone/', response_model=PhonesShem)
async def delete_phone(_id: int):
    query = phones.delete().where(phones.c.id == _id)
    logger.warning("phone create")
    return await database.execute(query)
