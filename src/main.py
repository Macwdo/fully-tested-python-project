from fastapi import FastAPI

from src.routes.records_routes import router as records_router

app = FastAPI()

app.include_router(records_router, prefix='/records')
