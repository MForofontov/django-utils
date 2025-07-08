from django.http import HttpResponsePermanentRedirect

class HTTPSRedirectMiddleware:
    """
    Middleware to redirect HTTP requests to HTTPS.
    
    This middleware ensures that all incoming HTTP requests are redirected to HTTPS.
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
        Handle the incoming request and redirect to HTTPS if the request is not secure.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response, potentially redirected to HTTPS.
        """
        # Check if the request is not secure (HTTP)
        if not request.is_secure():
            # Build the secure URL by replacing 'http://' with 'https://'
            secure_url = request.build_absolute_uri(request.get_full_path()).replace("http://", "https://")
            # Redirect to the secure URL
            return HttpResponsePermanentRedirect(secure_url)
        # Pass the request to the next middleware or view
        return self.get_response(request)
