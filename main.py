from contextlib import asynccontextmanager

from pydantic import BaseModel

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import requests as rq

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    print('Bot is ready')
    yield


app = FastAPI(title='To do APP', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
    allow_credentail=True,
    allow_methods=['*']
    allow_headers=['*']

)

@app.get('/api/tasks/{tg_id}')
async def tasks(tg_id: int):
    user= await rq.add_user(tg_id)
async def profile(tg_id:int):
    user=await rq.add_user(tg_id)




@app.get('/api/main/{tg_id}')
async def profile(tg_id:int):
    user= await rq.add_user(tg_id)
    completed_tasks_count =await rq.get_omplited_tasks_count(user.id)
    return {'completedTasks': completed_tasks_count}