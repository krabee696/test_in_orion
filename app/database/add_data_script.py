from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from database import engine, metadata
import csv

# Скрипт для заполнения базы данных (по 10 всего) из cvs файла

# Загрузка всех доступных определений таблиц из базы данных
# Генерирует новые Session (управляет операциями сохраняемости 
# для объектов, отображаемых с помощью ORM) объекты при вызове, 
# создавая их с учетом установленных здесь конфигурационных аргументов: 
# autocommit - настройка автоматической фиксации для использования с созданными Session объектами,
# autoflush - параметр автоматической очистки для использования с созданными Session объектами,
# bind - Engine, с которым будут связаны созданные объекты Session
metadata.reflect(engine, only=['users', 'phones', 'mails'])
Session = sessionmaker(autocommit=True, autoflush=False, bind=engine)

# Aвтоматически генерирует сопоставленные классы и отношения из схемы базы данных, 
# как правило, хотя и не обязательно отраженной.
Base = automap_base(metadata=metadata)
Base.prepare()
users, phones, mails = Base.classes.users, Base.classes.phones, Base.classes.mails

# Заполнение Users
# Полное описание заолнения ддля Users, остальные действуют аналогично
# Используется конструкция with...as для -гарантии того, что после открытия 
# файл будет закрыт. В фун-ии open() описан путь к файлу и кодировка.
# Возвращает объект чтения, который будет перебирать строки в заданном csvfile. 
# Возвращает строку каждый раз, когда вызывается его next() метод. 
# Откртие session. Создание пустого листа (objs[]). delimiter="" - удаление разделяющих символов.
# Добавление циклом for...in данных из csv.Выполните массовое сохранение заданного списка объектов.
# Функция массового сохранения (bulk_save_objects) позволяет использовать сопоставленные объекты 
# в качестве источника простых операций INSERT и UPDATE. После закрытие session.
with open('app/database/data/users_ex.csv', encoding='utf-8') as f:
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
with open('app/database/data/phone_ex.csv', encoding='utf-8') as f:
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
with open('app/database/data/mail_ex.csv', encoding='utf-8') as f:
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
