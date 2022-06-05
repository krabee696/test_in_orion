from views.mail import mails_router
from views.phone import phone_router
from views.user import users_router


def register_route(app):
    app.include_router(users_router)
    app.include_router(mails_router)
    app.include_router(phone_router)
