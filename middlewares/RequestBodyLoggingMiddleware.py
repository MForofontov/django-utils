import logging

# Initialize the logger for this module
logger = logging.getLogger(__name__)

class RequestBodyLoggingMiddleware:
    """
    Middleware to log the request body for POST and PUT requests.

    This middleware logs the body of incoming HTTP requests if the request method is POST or PUT.
    It can be useful for debugging purposes to see the data being sent to the server.
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
        Handle the incoming request and log the request body for POST and PUT requests.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Check if the request method is POST or PUT
        if request.method in ['POST', 'PUT']:
            # Log the request body
            logger.info(f'Request body: {request.body}')
        
        # Call the next middleware or view
        return self.get_response(request)
