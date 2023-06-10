from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.monitoreo import monitoreo

app = FastAPI()

app.include_router(monitoreo)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)