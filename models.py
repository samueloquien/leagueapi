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
    is_active: bool = True
    is_admin: bool = False

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Peter",
                "last_name": "Parker",
                "email": "spiderman@marvel.org",
                "password": "53cr3t-w0rd",
                "alias": "spiderman",
                "is_active": True,
                "is_admin": False
            }
        }

class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    alias: Optional[str]
    is_active: Optional[bool]
    is_admin: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Peter",
                "last_name": "Parker",
                "email": "spiderman@marvel.org",
                "password": "53cr3t-w0rd",
                "alias": "spiderman",
                "is_active": True,
                "is_admin": False
            }
        }

