import logging
from datetime import datetime

# Setting up a logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('requests.log')  # Log file
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user or 'Anonymous'
        user = request.user if request.user.is_authenticated else "Anonymous"

        # Log the request
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        # Continue processing the request
        response = self.get_response(request)
        return response
