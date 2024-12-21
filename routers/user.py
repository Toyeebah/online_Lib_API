from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import  Optional
from schemas.user import User,users,UserResponse,UserCreate
from CRUD.user import UserCrud


user_router = APIRouter()



# Create a new user
@user_router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate):
   return UserCrud.create_user(user_data)


# Get a user by ID
@user_router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    return UserCrud.get_user_by_id(user_id)

# Get a user 
@user_router.get("/", response_model=UserResponse)
def get_user():
    return UserCrud.get_user()


# Update a user
@user_router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, new_data: UserCreate):
    return UserCrud.update_user(user_id, new_data)


# Delete a user
@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    return UserCrud.delete_user(user_id)


# Deactivate a user
@user_router.post("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    return UserCrud.deactivate_user(user_id)


