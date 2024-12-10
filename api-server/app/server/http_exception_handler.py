import logging

from fastapi.responses import JSONResponse

logger = logging.getLogger("app.http_exc_handler")


async def http_exception_handler(request, exc):
    logger.error(
        f"[request_id: {request.state.request_id}, method:{request.method}, path: {request.url}] "
        f"Failed to handle request. "
        f"status_code={exc.status_code}, detail={exc.detail}  "
    )
    # Return the original response to the client
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
