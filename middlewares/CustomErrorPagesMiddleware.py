from django.http import HttpResponseRedirect

class CustomErrorPagesMiddleware:
    """
    Middleware to redirect to custom error pages for specific HTTP status codes.
    
    This middleware redirects to custom error pages when a 404 or 500 status code
    is encountered in the response.
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
        Handle the incoming request and redirect to custom error pages if needed.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response, potentially redirected to a custom error page.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Check if the response status code is 404
        if response.status_code == 404:
            # Redirect to the custom 404 error page
            return HttpResponseRedirect('/404/')
        # Check if the response status code is 500
        elif response.status_code == 500:
            # Redirect to the custom 500 error page
            return HttpResponseRedirect('/500/')
        # Return the original response if no redirection is needed
        return response
