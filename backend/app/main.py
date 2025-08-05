from fastapi import FastAPI

app=FastAPI( title="EdTech Adaptive Learning Platform API",
    version="1.0.0",
    description="Backend service for personalized learning paths, assessments, and feedback.")

@app.get("/")
async def root():
    return {"message":"Welcome to EdTech Adaptive Learning Platform API"}