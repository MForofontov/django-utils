class SEOOptimizationMiddleware:
    """
    Middleware to add SEO optimization headers to HTTP responses.

    This middleware adds the 'X-Robots-Tag' and 'X-UA-Compatible' headers to all HTTP responses
    to improve SEO and compatibility with Internet Explorer.
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
        Handle the incoming request and add SEO optimization headers to the response.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response with SEO optimization headers added.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)
        # Add the 'X-Robots-Tag' header to control search engine indexing
        response["X-Robots-Tag"] = "index, follow"
        # Add the 'X-UA-Compatible' header for Internet Explorer compatibility
        response["X-UA-Compatible"] = "IE=edge"
        return response
