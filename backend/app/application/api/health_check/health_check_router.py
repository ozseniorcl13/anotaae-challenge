from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

health_check_router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@health_check_router.get(
    "",
    summary="Return health check of system",
    status_code=200,
)
async def health_check(req: Request) -> Response:
    return Response(status_code=200)
