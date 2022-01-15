from api import app

from .health import router as health_router

app.include_router(health_router)
