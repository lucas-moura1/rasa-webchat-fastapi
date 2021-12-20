import logging
import sys

from asgi_correlation_id.context import correlation_id

from src.utils.constants import LOG_LEVEL

class LogFormatter(logging.Formatter):

    def format(self, record):
        record.request_id = correlation_id.get()

        return super(LogFormatter, self).format(record)


handler = logging.StreamHandler(sys.stdout)


handler.setFormatter(
    LogFormatter("[%(asctime)s] [%(filename)s] [%(levelname)s] [%(request_id)s] - "
                 "%(message)s")
)

logging.getLogger().setLevel(LOG_LEVEL)
logging.getLogger().addHandler(handler)
