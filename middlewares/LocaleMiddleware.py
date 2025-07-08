from django.utils import translation

class LocaleMiddleware:
    """
    Middleware to set the locale based on a cookie.
    
    This middleware sets the locale for the current request based on the 'user_locale'
    cookie. If the cookie is not present, it defaults to 'en' (English).
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
        Handle the incoming request and set the locale based on the 'user_locale' cookie.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the locale from the 'user_locale' cookie, default to 'en' if not present
        user_locale = request.COOKIES.get('user_locale', 'en')
        # Activate the specified locale
        translation.activate(user_locale)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Deactivate the locale after the response is generated
        translation.deactivate()
        return response
