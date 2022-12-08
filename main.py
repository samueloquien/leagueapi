from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import book_router, user_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    print('Ready to start mongodb client')
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print('Connected to db', app.database)

@app.on_event("shutdown")
def shutdown_db_client():
    print('Closing client')
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(user_router, tags=["users"], prefix="/user")

