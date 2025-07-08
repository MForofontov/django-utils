from django.http import JsonResponse

class JsonResponseMiddleware:
    """
    Middleware to convert responses to JSON format for API endpoints.
    
    This middleware converts the response to JSON format if the request path starts
    with '/api/' and the response status code is 200.
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
        Handle the incoming request and convert the response to JSON format if applicable.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response, potentially converted to JSON format.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Check if the response status code is 200 and the request path starts with '/api/'
        if response.status_code == 200 and request.path.startswith('/api/'):
            # Convert the response to JSON format
            return JsonResponse(response.data, safe=False)  # Assuming response.data is already a dict
        # Return the original response if no conversion is needed
        return response
