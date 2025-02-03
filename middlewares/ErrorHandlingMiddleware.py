import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("your_logger_name")

class ErrorHandlingMiddleware(MiddlewareMixin):
    """
    Middleware to handle exceptions and return a JSON response with an error message.
    """
    def process_exception(self, request, exception):
        """
        Process exceptions and return a JSON response with an error message.

        Parameters
        ----------
        request : HttpRequest
            The HTTP request object.
        exception : Exception
            The exception that was raised.

        Returns
        -------
        JsonResponse
            A JSON response with an error message and status code.
        """
        # Log the exception with traceback
        logger.error(f"Exception occurred: {exception}", exc_info=True)
        
        # Prepare the response data
        response_data = {
            "error": "An unexpected error occurred.",
            "details": str(exception)
        }
        
        # Return the JSON response with status code 500
        return JsonResponse(request)