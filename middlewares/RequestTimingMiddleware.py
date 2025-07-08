import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    """
    Middleware to log the duration of each HTTP request.
    
    This middleware logs the time taken to process each HTTP request. It is useful
    for monitoring the performance of the application.
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
        Handle the incoming request and log the duration of the request processing.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Record the start time of the request
        start_time = time.time()
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Calculate the duration of the request processing
        duration = time.time() - start_time
        # Log the duration of the request processing
        logger.info(f'Request to {request.path} took {duration:.2f} seconds')
        return response
