import logging

logger = logging.getLogger(__name__)

class ResponseLoggingMiddleware:
    """
    Middleware to log the data being sent to the user in the response.
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
        Handle the incoming request and get the response.
        
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
        
        # Log the response data
        self.log_response(response)
        
        # Return the response
        return response

    def log_response(self, response):
        """
        Log the response data.
        
        Parameters
        ----------
        response : HttpResponse
            The HTTP response to be logged.
        """
        try:
            # Decode the response content and log it
            response_content = response.content.decode('utf-8')
            logger.info(f"Response data: {response_content}")
        except Exception as e:
            # Log any errors that occur during logging
            logger.error(f"Error logging response data: {e}")