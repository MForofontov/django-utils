from django.utils import timezone

class TimezoneMiddleware:
    """
    Middleware to set the timezone based on a cookie.
    
    This middleware sets the timezone for the current request based on the 'timezone'
    cookie. If the cookie is not present, it defaults to 'UTC'.
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
        Handle the incoming request and set the timezone based on the 'timezone' cookie.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the timezone name from the 'timezone' cookie, default to 'UTC' if not present
        timezone_name = request.COOKIES.get('timezone', 'UTC')
        # Activate the specified timezone
        timezone.activate(timezone_name)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Deactivate the timezone after the response is generated
        timezone.deactivate()
        return response
