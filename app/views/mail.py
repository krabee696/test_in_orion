from typing import List
from logs import logger
from shema import MailsShem
from fastapi import APIRouter
from database.database import mails, database

# Вызов роутеров для почты
mails_router = APIRouter()


# Создание Mails
@mails_router.put("/mail/", response_model=MailsShem)
async def create_mail(mail: MailsShem):
    query = mails.insert().values(
        type_mail=mail.type_mail,
        address_mail=mail.address_mail,
        user_id=mail.user_id
    )
    logger.warning("mail create")
    mail.id = await database.execute(query)
    return mail


# Чтение всех Mails
@mails_router.post('/mail/', response_model=List[MailsShem])
async def read_all_mail():
    query = mails.select()
    return await database.fetch_all(query)


# Чтение Mails по id
@mails_router.post('/mail/{mail_id}/', response_model=MailsShem)
async def read_phone(_id: int):
    query = mails.select().where(mails.c.id == _id)
    return await database.fetch_one(query)


# Изменение Mails
@mails_router.patch('/mail/', response_model=MailsShem)
async def update_phone(mail: MailsShem, _id: int):
    query = mails.update().where(mails.c.id == _id).values(
        type_mail=mail.type_mail,
        address_mail=mail.address_mail,
        user_id=mail.user_id
    )
    logger.warning("mail update")
    await database.execute(query)
    return mail


# Удаление Mails
@mails_router.delete('/mail/', response_model=MailsShem)
async def delete_mail(_id: int):
    query = mails.delete().where(mails.c.id == _id)
    logger.warning("mail delete")
    return await database.execute(query)
