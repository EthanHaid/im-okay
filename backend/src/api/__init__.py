from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config

app = FastAPI(docs_url="/", root_path="/prod")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://imokay.tech"
        "https://www.imokay.tech"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from . import routes, models
