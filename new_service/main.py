from fastapi import FastAPI

app = FastAPI()

# Simple endpoint to verify the service is running
@app.get("/")
def hello_world():
    return {"Hello World from New Service!"}
