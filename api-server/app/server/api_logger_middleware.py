import json
import logging
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

# Initialize the logger
logger = logging.getLogger("app.api_logger")


# Custom Middleware for Logging on API request
class APILoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Generate a unique request_id
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id  # Attach to the request state

        # Log the incoming request
        start_time = time.time()
        body = await request.body()
        try:
            # Try to load JSON and log it in compact form
            body_json = json.loads(body)
            compact_body = json.dumps(body_json, separators=(",", ":"))
        except json.JSONDecodeError:
            # Fallback to plain text if not valid JSON
            compact_body = body.decode("utf-8")
        logger.info(
            f"[request_id: {request_id}, method:{request.method}, path: {request.url}] "
            f"Request body: {compact_body}."
        )

        response = await call_next(request)
        return response
