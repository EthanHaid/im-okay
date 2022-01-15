import uvicorn

from api import app

if __name__ == "__main__":
    uvicorn.run("asgi:app", reload=True)
