class ContentSecurityPolicyMiddleware:
    """
    Middleware to add Content Security Policy (CSP) headers to HTTP responses.
    
    This middleware adds a Content Security Policy (CSP) header to all HTTP responses
    to enhance the security of the application by preventing various types of attacks.
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
        Handle the incoming request and add the CSP header to the response.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response with the CSP header added.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Add the Content Security Policy (CSP) header to the response
        response['Content-Security-Policy'] = "default-src 'self';"
        return response
