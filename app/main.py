from fastapi import FastAPI
from app.api.v1 import products

app = FastAPI(title="Online Shop")

app.include_router(products.router, prefix="/products", tags=["products"])
