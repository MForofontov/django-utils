from django.utils import translation

class BrowserLanguageDetectionMiddleware:
    """
    Middleware to detect and switch the language based on the browser's Accept-Language header.
    
    This middleware reads the 'HTTP_ACCEPT_LANGUAGE' header from the request and activates
    the first language specified in the header.
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
        Handle the incoming request and switch the language based on the browser's Accept-Language header.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the language code from the 'HTTP_ACCEPT_LANGUAGE' header
        lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en').split(',')[0]
        # Activate the detected language
        translation.activate(lang)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Deactivate the language after the response is generated
        translation.deactivate()
        return response
