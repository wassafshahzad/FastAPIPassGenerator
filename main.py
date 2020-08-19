from fastapi import FastAPI
from password_gen import routes


app = FastAPI()

app.include_router(routes.router)
