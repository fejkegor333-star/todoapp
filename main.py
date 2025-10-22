# # from contextlib import asynccontextmanager
# # from pydantic import BaseModel
# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware
# # from models import init_db
# # import requests as rq  # ⚠️ если это твой модуль, переименуй его, чтобы не путать с requests

# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     await init_db()
# #     print('Bot is ready')
# #     yield

# # app = FastAPI(title='To do APP', lifespan=lifespan)

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=['*'],
# #     allow_credentials=True,
# #     allow_methods=['*'],
# #     allow_headers=['*']
# # )

# # @app.get('/api/tasks/{tg_id}')
# # async def tasks(tg_id: int):
# #     user = await rq.add_user(tg_id)
# #     return {"message": f"Tasks for user {tg_id}"}  # пример возврата

# # @app.get('/api/main/{tg_id}')
# # async def main(tg_id: int):
# #     user = await rq.add_user(tg_id)
# #     completed_tasks_count = await rq.get_omplited_tasks_count(user.id)
# #     return {"completedTasks": completed_tasks_count}


# # from fastapi import FastAPI

# # app = FastAPI()

# # @app.get("/")
# # def read_root():
# #     return {"message": "Hello, world!"}

# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from models import init_db
# import requests as rq  # твой асинхронный модуль

# class AddTask(BaseModel):
#     tg_id: int 
#     title: str

# class CompleteTask(BaseModel):
#     id: int

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await init_db()
#     print("Bot is ready")
#     yield

# app = FastAPI(title="To do APP", lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# @app.get("/api/tasks/{tg_id}")
# async def tasks(tg_id: int):
#     user = await rq.add_user(tg_id)
#     return {"message": f"Tasks for user {tg_id}"}

# @app.get("/api/main/{tg_id}")
# async def main(tg_id: int):
#     user = await rq.add_user(tg_id)
#     completed_tasks_count = await rq.get_completed_tasks_count(user.id)
#     return {"completedTasks": completed_tasks_count}

# @app.get("/")
# async def read_root():
#     return {"message": "Hello, world!"}

# @app.post("/api/add")
# async def add_task(task: AddTask):
#     user = await rq.add_user(task.tg_id)
#     await rq.add_task(user.id, task.title)
#     return {"status": "ok"}

# @app.patch("/api/complited")
# async def complete_task(task: CompleteTask):
#     await rq.update_task(task.id)
#     return {"status": "ok"}

from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import requests as rq


class AddTask(BaseModel):
    tg_id: int
    title: str


class CompleteTask(BaseModel):
    id: int


@asynccontextmanager
async def lifespan(app_: FastAPI):
    await init_db()
    print('Bot is ready')
    yield


app = FastAPI(title="To Do App", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/tasks/{tg_id}")
async def tasks(tg_id: int):
    user = await rq.add_user(tg_id)
    return await rq.get_tasks(user.id)


@app.get("/api/main/{tg_id}")
async def profile(tg_id: int):
    user = await rq.add_user(tg_id)
    completed_tasks_count = await rq.get_completed_tasks_count(user.id)
    return {'completedTasks': completed_tasks_count}


@app.post("/api/add")
async def add_task(task: AddTask):
    user = await rq.add_user(task.tg_id)
    await rq.add_task(user.id, task.title)
    return {'status': 'ok'}


@app.patch("/api/completed")
async def complete_task(task: CompleteTask):
    await rq.update_task(task.id)
    return {'status': 'ok'}