class HeaderRemovalMiddleware:
    """
    Middleware to remove specific headers from HTTP requests.

    This middleware removes the 'X-Powered-By' header from incoming HTTP requests
    to enhance security by obscuring the server technology.
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
        Handle the incoming request and remove the 'X-Powered-By' header if present.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Check if the 'X-Powered-By' header is present in the request
        if "X-Powered-By" in request.META:
            # Remove the 'X-Powered-By' header
            del request.META["X-Powered-By"]
        # Get the response from the next middleware or view
        return self.get_response(request)
