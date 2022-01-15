from fastapi import FastAPI

app = FastAPI(docs_url="/", root_path="/prod")

from . import routes, models
