from fastapi import FastAPI
from app.routers import user_router
from app.routers import movie_router
from app.routers import user_movie_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(movie_router.router)
app.include_router(user_movie_router.router)

@app.get("/")
def read_root():
    return {"Project is running"}