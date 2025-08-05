from fastapi import FastAPI
from .routers import auth
app=FastAPI( title="EdTech Adaptive Learning Platform API",
    version="1.0.0",
    description="Backend service for personalized learning paths, assessments, and feedback.")
app.include_router(auth.router,prefix="/api/v1/auth",tags=["Auth"])

@app.get("/")
async def root():
    return {"message":"Welcome to EdTech Adaptive Learning Platform API"}