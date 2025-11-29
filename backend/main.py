from fastapi import FastAPI

app = FastAPI(title="MindForge AI API")

@app.get("/")
def read_root():
    return {"message": "Welcome to MindForge AI API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
