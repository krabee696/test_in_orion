import databases
import sqlalchemy as sa
from sqlalchemy.schema import ForeignKey

# Подключение к БД и ее развертывание

# database_ur = "dialect+driver://username:password@host:port/database"
DATABASE_URL = "postgresql://postgres:1223@localhost:5432/address_book"

# Созание объектов хранящих DATABASE_URL и MetaData
# Объект MetaData содержит все конструкции схемы, которые мы с ним связали
database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

# Описание сущности users
users = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('full_name', sa.String),
    sa.Column('gender', sa.String),
    sa.Column('birth_day', sa.Date),
    sa.Column('address', sa.String)
)

# Описание сущности phones
phones = sa.Table(
    'phones',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('type_phone', sa.String),
    sa.Column('number_phone', sa.String),
    sa.Column('user_id', sa.Integer, ForeignKey('users.id', ondelete='CASCADE'))
)

# Описание сущности mails
mails = sa.Table(
    'mails',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('type_mail', sa.String),
    sa.Column('address_mail', sa.String),
    sa.Column('user_id', sa.Integer, ForeignKey('users.id', ondelete='CASCADE'))
)

# Cоздания объекта Engine именно он отвечает за взаимодействие с базой данных
# Создание всех конструкций схем, которые мы описали и связали с MetaData выше
engine = sa.create_engine(DATABASE_URL)
metadata.create_all(engine)

