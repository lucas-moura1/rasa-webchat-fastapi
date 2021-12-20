from typing import Optional
import logging

from fastapi import FastAPI
from asgi_correlation_id import CorrelationIdMiddleware

from src.utils import logger

app = FastAPI()
app.add_middleware(CorrelationIdMiddleware)


from src.routes import weather_routes
