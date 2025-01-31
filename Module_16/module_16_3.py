from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def user() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create(
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter Username', example='Ivan')]
        , age: Annotated[int, Path(ge=18, le=100, description='Enter age', example=30)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered!'


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id: Annotated[int, Path(ge=1, le=100, description='Enter user_id', example=30)]
                 , username: Annotated[
            str, Path(min_length=3, max_length=15, description='Enter Username', example='Ivan')]
                 , age: Annotated[int, Path(ge=18, le=100, description='Enter age', example=30)]) -> str:
    users[user_id] = (f'Имя: {username}, возраст: {age}')
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id) -> str:
    users.pop(user_id)
    return f'The user {user_id} is deleted'
