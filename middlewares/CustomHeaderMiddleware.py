class CustomHeaderMiddleware:
    """
    Middleware to add a custom header to HTTP responses.

    This middleware adds an 'X-Custom-Header' with a predefined value
    to every HTTP response.
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
        Handle the incoming request and add a custom header to the response.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response with the custom header added.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Add the custom header to the response
        response["X-Custom-Header"] = "MyValue"
        return response
