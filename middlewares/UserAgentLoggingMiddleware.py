import logging

logger = logging.getLogger(__name__)


class UserAgentLoggingMiddleware:
    """
    Middleware to log the User-Agent header for each HTTP request.

    This middleware logs the User-Agent header of each incoming HTTP request.
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
        Handle the incoming request and log the User-Agent header.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the User-Agent header from the request
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        # Log the User-Agent header
        logger.info(f"User Agent: {user_agent}")
        # Get the response from the next middleware or view
        response = self.get_response(request)
        return response
