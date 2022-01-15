from api import app

from .health import router as health_router
from.messaging import router as messaging_router

app.include_router(health_router)
app.include_router(messaging_router)
