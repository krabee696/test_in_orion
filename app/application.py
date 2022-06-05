from fastapi import FastAPI
from database.database import database
from routes import register_route


app = FastAPI()


@app.on_event("startup")
async def startup():
    register_route(app)
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


