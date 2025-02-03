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
        
        # Process the response
        self.process_response(request, response)
        
        # Return the response
        return response

    def process_response(self, request, response):
        """
        Process the response and log the data being sent to the user.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        response : HttpResponse
            The HTTP response object.
        
        Returns
        -------
        HttpResponse
            The HTTP response object.
        """
        # Log the response data
        try:
            # Decode the response content and log it
            response_content = response.content.decode('utf-8')
            logger.info(f"Response data: {response_content}")
        except Exception as e:
            # Log any errors that occur during logging
            logger.error(f"Error logging response data: {e}")

        # Return the response
        return response