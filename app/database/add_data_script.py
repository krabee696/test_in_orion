from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from app.database.database import engine, metadata
import csv

# Скрипт для заполнения базы данных (по 10 всего) из cvs файла

metadata.reflect(engine, only=['users', 'phones', 'mails'])
Session = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = automap_base(metadata=metadata)
Base.prepare()


users, phones, mails = Base.classes.users, Base.classes.phones, Base.classes.mails

# Заполнение Users
with open('data/users_ex.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    session = Session()
    objs = []
    for row in reader:
        obj = users(
            full_name=row[0],
            gender=row[1],
            birth_day=row[2],
            address=row[3]
        )
        objs.append(obj)

    session.bulk_save_objects(objs)
    session.close()

# Заполнение Phone
with open('data/phone_ex.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    session = Session()
    objs = []
    for row in reader:
        obj = phones(
            type_phone=row[0],
            number_phone=row[1],
            user_id=row[2]
        )
        objs.append(obj)
    session.bulk_save_objects(objs)
    session.close()

# Заполнение Mail
with open('data/mail_ex.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    session = Session()
    objs = []
    for row in reader:
        obj = mails(
            type_mail=row[0],
            address_mail=row[1],
            user_id=row[2]
        )
        objs.append(obj)
    session.bulk_save_objects(objs)
    session.close()
