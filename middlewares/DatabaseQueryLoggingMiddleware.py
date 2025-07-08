import logging
from django.db import connection

logger = logging.getLogger(__name__)

class DatabaseQueryLoggingMiddleware:
    """
    Middleware to log database queries for each HTTP request.
    
    This middleware logs all database queries executed during the processing
    of an HTTP request. It is useful for debugging and performance monitoring.
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
        Handle the incoming request and log the database queries.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Retrieve the list of database queries executed during the request
        queries = connection.queries
        # Log the database queries
        logger.info(f'Database queries: {queries}')
        return response
