from django.http import HttpResponse

class CORSPrefightMiddleware:
    """
    Middleware to handle CORS preflight requests.
    
    This middleware intercepts HTTP OPTIONS requests and adds the necessary
    CORS headers to the response. This is useful for enabling cross-origin
    requests in a Django application.
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
        Handle the incoming request. If the request method is OPTIONS, return
        a response with the appropriate CORS headers. Otherwise, pass the 
        request to the next middleware or view.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response with CORS headers if the method is OPTIONS,
            otherwise the response from the next middleware or view.
        """
        if request.method == 'OPTIONS':
            # Create an empty HTTP response
            response = HttpResponse()
            # Add CORS headers to the response
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            return response
        
        # Pass the request to the next middleware or view
        return self.get_response(request)
