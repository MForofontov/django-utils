class TokenToAuthorizationHeaderMiddleware:
    """
    Middleware to transfer token from cookie to Authorization header.

    This middleware extracts the token from an HTTP-only cookie named 'accessToken'
    and adds it to the request headers as an Authorization header.
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
        Handle the incoming request and add the token to the Authorization header.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Extract the token from the HTTP-only cookie
        token = request.COOKIES.get("accessToken")
        if token:
            # Add the token to the request headers
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        # Get the response from the next middleware or view
        return self.get_response(request)
