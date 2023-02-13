from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routers import users
#from auth import auth

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    print('Ready to start mongodb client')
    app.mongodb_client = MongoClient(config["ATLAS_URI"],
        tls=True, tlsAllowInvalidCertificates=True)
    app.database = app.mongodb_client[config["DB_NAME"]]
    print('Connected to db', app.database)

@app.on_event("shutdown")
def shutdown_db_client():
    print('Closing client')
    app.mongodb_client.close()

app.include_router(users.router, tags=["users"], prefix="/users")
#app.include_router(auth, tags=["auth"], prefix="/auth")

