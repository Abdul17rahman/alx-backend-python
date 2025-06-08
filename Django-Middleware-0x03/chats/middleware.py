import logging
from datetime import datetime, time

from django.http import HttpResponseForbidden

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

    class RestrictAccessByTimeMiddleware:

        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Define allowed access time range (6 PM to 9 PM)
            current_time = datetime.now().time()
            start_time = time(18, 0)  # 6:00 PM
            end_time = time(21, 0)    # 9:00 PM

            # Check if request is to the messaging/chat endpoints
            if "/messages" in request.path or "/conversations" in request.path:
                if not (start_time <= current_time <= end_time):
                    return HttpResponseForbidden("Access to chat is only allowed between 6:00 PM and 9:00 PM.")

            return self.get_response(request)
