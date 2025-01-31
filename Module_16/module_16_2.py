from fastapi import FastAPI, Path
from typing import Annotated

MyApp = FastAPI()


@MyApp.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@MyApp.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@MyApp.get("/user/{user_id}")
async def user_page(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@MyApp.get("/user/{username}/{age}")
async def data_page(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:
    return {'Информация о пользователе. Имя': username, 'Возраст': age}
