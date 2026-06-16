from fastapi import FastAPI

from app.tasks.router import router as tasks_router


def create_app() -> FastAPI:
    app = FastAPI(title="Mini Tasks API")
    app.include_router(tasks_router)
    return app


app = create_app()

