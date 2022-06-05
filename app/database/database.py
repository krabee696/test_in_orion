import databases
import sqlalchemy as sa
from sqlalchemy.schema import ForeignKey

# Подключение к БД и ее развертывание

DATABASE_URL = "postgresql://postgres:1223@localhost:5432/address_book"

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

users = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('full_name', sa.String),
    sa.Column('gender', sa.String),
    sa.Column('birth_day', sa.Date),
    sa.Column('address', sa.String)
)

phones = sa.Table(
    'phones',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('type_phone', sa.String),
    sa.Column('number_phone', sa.String),
    sa.Column('user_id', sa.Integer, ForeignKey('users.id', ondelete='CASCADE'))
)

mails = sa.Table(
    'mails',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('type_mail', sa.String),
    sa.Column('address_mail', sa.String),
    sa.Column('user_id', sa.Integer, ForeignKey('users.id', ondelete='CASCADE'))
)

engine = sa.create_engine(DATABASE_URL)

