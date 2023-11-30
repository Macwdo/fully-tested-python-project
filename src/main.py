from fastapi import FastAPI

from src.routes.records import router as records_router

app = FastAPI()

app.include_router(records_router, prefix='/records')
