import uuid
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    alias: str = Field(...)
    is_admin: bool = False

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Peter",
                "last_name": "Parker",
                "email": "spiderman@marvel.org",
                "password": "53cr3t-w0rd",
                "alias": "spiderman"
            }
        }

class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    alias: Optional[str]
    is_admin: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Peter",
                "last_name": "Parker",
                "email": "spiderman@marvel.org",
                "password": "53cr3t-w0rd",
                "alias": "spiderman"
            }
        }



class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }