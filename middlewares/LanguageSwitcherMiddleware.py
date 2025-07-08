from django.utils import translation


class LanguageSwitcherMiddleware:
    """
    Middleware to switch the language based on the request parameter.

    This middleware allows switching the language of the application based on
    a 'lang' parameter in the request's query string.
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
        Handle the incoming request and switch the language if the 'lang' parameter is present.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the language code from the query parameters
        lang_code = request.GET.get("lang")
        if lang_code:
            # Activate the specified language
            translation.activate(lang_code)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Deactivate the language after the response is generated
        translation.deactivate()
        return response
