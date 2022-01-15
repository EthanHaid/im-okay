from fastapi import FastAPI

app = FastAPI(docs_url="/")

from . import routes, models
