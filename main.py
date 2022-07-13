from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import cars, reviews, user
from sql import models
from sql.database import engine

app = FastAPI()

origins = {
    "*"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(cars.router)
app.include_router(reviews.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}