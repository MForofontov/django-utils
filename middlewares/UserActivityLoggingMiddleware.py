import logging

logger = logging.getLogger(__name__)

class UserActivityLoggingMiddleware:
    """
    Middleware to log user activity for each HTTP request.
    
    This middleware logs the activity of authenticated users, including the username
    and the path accessed, for each HTTP request.
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
        Handle the incoming request and log the user activity if the user is authenticated.
        
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
        
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Log the username and the path accessed
            logger.info(f'User {request.user.username} accessed {request.path}')
        
        return response
