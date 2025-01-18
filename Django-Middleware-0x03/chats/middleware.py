import logging
import time
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from collections import defaultdict

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



class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store message counts and timestamps for each IP
        self.ip_message_log = defaultdict(list)

        # Define message limit and time window
        self.MESSAGE_LIMIT = 5
        self.TIME_WINDOW = 60  # 1 minute in seconds

    def __call__(self, request):
        # Only apply the limit for POST requests to the messaging endpoint
        if request.method == "POST" and "messaging" in request.path:
            ip_address = self.get_client_ip(request)
            current_time = time.time()

            # Retrieve or initialize the message log for the IP
            message_times = self.ip_message_log[ip_address]

            # Remove messages outside the time window
            self.ip_message_log[ip_address] = [
                timestamp for timestamp in message_times if current_time - timestamp <= self.TIME_WINDOW
            ]

            # Check if the user has exceeded the limit
            if len(self.ip_message_log[ip_address]) >= self.MESSAGE_LIMIT:
                return HttpResponseForbidden("You have exceeded the messaging limit. Please try again later.")

            self.ip_message_log[ip_address].append(current_time)

        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        """Extracts the client's IP address from the request."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip


class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user's role from the request (adjust based on your model)
            user_role = getattr(request.user, 'role', None)

            # Define roles that are allowed
            allowed_roles = ['admin', 'moderator']

            if user_role not in allowed_roles:
                return HttpResponseForbidden("You do not have permission to perform this action.")
        
        return self.get_response(request)