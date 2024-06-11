import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from orm import create_tables, delete_tables
from router_location import location_router
from router_track import track_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(location_router)
app.include_router(track_router)
current_file_path = os.path.dirname(os.path.abspath(__file__))
print('current_file_path', current_file_path)
static_files_path = os.path.join(current_file_path, '../..', 'frontend', 'static')
print('static_files_path', static_files_path)

app.mount("/static", StaticFiles(directory=static_files_path), name="static")


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


