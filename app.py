from fastapi import FastAPI
from routes.monitoreo import monitoreo

app = FastAPI()

app.include_router(monitoreo)

