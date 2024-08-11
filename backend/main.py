import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.application.api.routes import api_routers
from app.infra.config.config import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.BACKEND_CORS_SETTINGS],
    allow_methods=["OPTIONS", "GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "x-access-token", "responseType"],
)

app.include_router(api_routers)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description=config.PROJECT_DESCRIPTION,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.HOST, port=config.PORT, reload=True)
