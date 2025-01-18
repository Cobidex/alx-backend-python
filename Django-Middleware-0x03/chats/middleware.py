import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

# Configure logging
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(message)s',
)

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the user's request information
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        # Proceed with the response
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current server time
        current_hour = datetime.now().hour

        start_hour = 21  # 9 PM
        end_hour = 6     # 6 AM

        if "messaging" in request.path:
            if current_hour >= start_hour or current_hour < end_hour:
                return HttpResponseForbidden("Access to the messaging app is restricted during this time.")

        response = self.get_response(request)
        return response
