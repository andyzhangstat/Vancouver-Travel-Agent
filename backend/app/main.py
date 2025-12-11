from fastapi import FastAPI
from app.api.routes_plan import router as plan_router

app = FastAPI(
    title="Vancouver Trip Planner API",
    version="1.0.0"
)

app.include_router(plan_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to Vancouver Trip Planner API!"}
