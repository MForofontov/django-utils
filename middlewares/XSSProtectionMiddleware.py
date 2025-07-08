class XSSProtectionMiddleware:
    """
    Middleware to add XSS protection headers to HTTP responses.
    
    This middleware adds the 'X-XSS-Protection' header to all HTTP responses to enable
    cross-site scripting (XSS) protection in the browser.
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
        Handle the incoming request and add the XSS protection header to the response.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response with the XSS protection header added.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Add the XSS protection header to the response
        response['X-XSS-Protection'] = '1; mode=block'
        return response
