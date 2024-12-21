
from fastapi import HTTPException
from schemas.user import UserCreate,users,User
from schemas.user import UserCreate, User, UserPatch, users


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = {"id": user_id, **user_data.dict()}
        users[user_id] = user
        return user

    @staticmethod
    def get_user_by_id(user_id: int):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return user


    @staticmethod
    def get_user():
        user = users.get()
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return user


    @staticmethod
    def update_user(user_id: int, new_data: UserCreate):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        users[user_id] = {"id": user_id, **new_data.dict()}
        return users[user_id]

    @staticmethod
    def delete_user(user_id: int):
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found.")
        del users[user_id]
        return {"detail": f"User {user_id} has been deleted."}

    @staticmethod
    def deactivate_user(user_id: int):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        user["is_active"] = False
        return {"detail": f"User {user_id} deactivated."}


user_crud = UserCrud()