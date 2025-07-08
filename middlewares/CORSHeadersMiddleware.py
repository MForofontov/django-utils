class CORSHeadersMiddleware:
    """
    Middleware to add CORS headers to HTTP responses.
    
    This middleware adds Cross-Origin Resource Sharing (CORS) headers to all HTTP responses
    to allow cross-origin requests from any domain.
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
        Handle the incoming request and add CORS headers to the response.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response with CORS headers added.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Add CORS headers to the response
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
