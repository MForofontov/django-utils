import logging

logger = logging.getLogger(__name__)

class QueryParameterLoggingMiddleware:
    """
    Middleware to log query parameters of incoming HTTP requests.
    
    This middleware logs the query parameters of each incoming HTTP request for debugging
    and monitoring purposes.
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
        Handle the incoming request and log the query parameters.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Log the query parameters of the request
        logger.info(f'Query parameters: {request.GET.dict()}')
        # Get the response from the next middleware or view
        return self.get_response(request)
