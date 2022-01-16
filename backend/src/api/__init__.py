from fastapi import FastAPI
from .config import config

app = FastAPI(docs_url="/", root_path="/prod")

from . import routes, models
