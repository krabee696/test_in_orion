from pydantic import BaseModel, validator
import datetime

# Конфигурационный класс
class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


# Схемы и валидаторы для полей БД
class PhonesShem(OurBaseModel):
    id: int
    type_phone: str
    number_phone: str
    user_id: int

    @validator('type_phone')
    def check_to_type_phone(cls, type_phone):
        if type_phone not in ['Городской', 'Мобильный']:
            raise ValueError('Incorrect type, must be Городской or Мобильный ')
        return type_phone

    @validator('number_phone')
    def check_to_length_number_phone(cls, number_phone):
        if 12 != len(number_phone):
            raise ValueError('Incorrect type, must be +OOOOOOOOOOO')
        return number_phone


class MailsShem(OurBaseModel):
    id: int
    type_mail: str
    address_mail: str
    user_id: int

    @validator('type_mail')
    def check_to_type_mail(cls, type_mail):
        if type_mail not in ['Личная', 'Рабочая']:
            raise ValueError('Incorrect type, must be Личная or Рабочая')
        return type_mail


class UsersShem(OurBaseModel):
    id: int
    full_name: str
    gender: str
    birth_day: datetime.date
    address: str

    @validator('gender')
    def check_to_type_gender(cls, gender):
        if gender not in ['Мужчина', 'Женщина']:
            raise ValueError('Incorrect type, must be Мужчина or Женщина')
        return gender

    @validator('full_name')
    def check_to_length_and_spaces_name(cls, full_name):
        if not 3 < len(full_name) < 99:
            raise ValueError('Incorrect length, must be in range 3 - 99')
        if ' ' not in full_name:
            raise ValueError('Incorrect input method, missing spaces')
        return full_name

    @validator('address')
    def check_to_length_address(cls, address):
        if not 3 < len(address) < 228:
            raise ValueError('Incorrect length, must be in range 3 - 228')
        return address
