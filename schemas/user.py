from pydantic import BaseModel,UUID4,EmailStr
from typing import Optional


class UserBase(BaseModel):
    id: UUID4
    name: str
    email: EmailStr
    is_active : bool = True

class User(UserBase):
    pass

class UserCreate(UserBase):
    id: UUID4
    name: str = "Toye"
    email: EmailStr ="tarow@yahoo.com"
    is_active : bool = True


class UserPatch(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    name: str
    is_active: bool


users: dict[int:User]= {}


    