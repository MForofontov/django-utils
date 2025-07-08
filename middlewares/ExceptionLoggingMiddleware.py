from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware:
    """
    Middleware to log exceptions for each HTTP request.

    This middleware logs any unhandled exceptions that occur during the processing
    of an HTTP request. It is useful for debugging and error monitoring.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable.

        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Handle the incoming request and log any unhandled exceptions.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view, or an error response
            if an unhandled exception occurs.
        """
        try:
            # Get the response from the next middleware or view
            response = self.get_response(request)
            return response
        except Exception as e:
            # Log the unhandled exception
            logger.error(f"Unhandled exception: {e}", exc_info=True)
            # Return an HTTP 500 Internal Server Error response
            return HttpResponse("Internal Server Error", status=500)
