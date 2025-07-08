import logging
from user_agents import parse

logger = logging.getLogger(__name__)

class UserDeviceLoggingMiddleware:
    """
    Middleware to log user device information for analytics.
    
    This middleware logs the user device information (e.g., browser, OS) from the User-Agent
    header of each incoming HTTP request for analytics purposes.
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
        Handle the incoming request and log the user device information.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Extract the User-Agent header from the request
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        # Parse the User-Agent string to get device information
        user_device = parse(user_agent)
        # Log the device information
        logger.info(f'User device: {user_device}')
        # Get the response from the next middleware or view
        return self.get_response(request)
