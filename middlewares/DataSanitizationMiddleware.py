import re

class DataSanitizationMiddleware:
    """
    Middleware to sanitize data in HTTP POST and PUT requests.
    
    This middleware removes HTML tags from the data in POST and PUT requests to prevent
    XSS (Cross-Site Scripting) attacks.
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
        Handle the incoming request and sanitize the data if the method is POST or PUT.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Check if the request method is POST or PUT
        if request.method in ['POST', 'PUT']:
            # Iterate over all POST data items
            for key, value in request.POST.items():
                # Remove HTML tags from the data
                request.POST[key] = re.sub(r'<[^>]*>', '', value)  # Simple HTML tag removal
        # Get the response from the next middleware or view
        return self.get_response(request)
