from fastapi import FastAPI

MyApp = FastAPI()


@MyApp.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@MyApp.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@MyApp.get("/user/{user_id}")
async def user_page(user_id:int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@MyApp.get("/user")
async def data_page(username: str, age: int) -> dict:
    return {'Информация о пользователе. Имя' : username,  'Возраст': age}
