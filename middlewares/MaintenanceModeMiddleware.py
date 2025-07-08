from django.http import HttpResponse

class MaintenanceModeMiddleware:
    """
    Middleware to enable maintenance mode for the application.
    
    This middleware returns a maintenance mode response for all incoming requests
    when the application is in maintenance mode.
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
        self.maintenance_mode = True  # Set to True to enable maintenance mode

    def __call__(self, request):
        """
        Handle the incoming request and return a maintenance mode response if enabled.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The maintenance mode response if enabled, otherwise the response from the next middleware or view.
        """
        if self.maintenance_mode:
            # Return a maintenance mode response
            return HttpResponse("The site is under maintenance. Please try again later.", status=503)
        
        # Pass the request to the next middleware or view
        return self.get_response(request)
