import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware:
    """
    Middleware to handle exceptions and return a JSON response with an error message.
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
        Handle the incoming request and process exceptions if they occur.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        try:
            # Get the response from the next middleware or view
            response = self.get_response(request)
        except Exception as exception:
            # Log the exception with traceback
            logger.error(f"Exception occurred: {exception}", exc_info=True)
            
            # Prepare the response data
            response_data = {
                "error": "An unexpected error occurred.",
                "details": str(exception)
            }
            
            # Return the JSON response with status code 500
            return JsonResponse(response_data, status=500)
        
        return response
