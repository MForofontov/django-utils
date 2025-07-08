from django.http import HttpResponsePermanentRedirect


class TrailingSlashMiddleware:
    """
    Middleware to ensure URLs end with a trailing slash.

    This middleware redirects requests to URLs that do not end with a trailing slash
    to the same URL with a trailing slash, except for URLs starting with '/admin/'.
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
        Handle the incoming request and redirect to a URL with a trailing slash if needed.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response, potentially redirected to a URL with a trailing slash.
        """
        # Check if the request path does not end with a slash and does not start with '/admin/'
        if not request.path.endswith("/") and not request.path.startswith(
            "/admin/"
        ):
            # Redirect to the same URL with a trailing slash
            return HttpResponsePermanentRedirect(request.path + "/")
        # Pass the request to the next middleware or view
        return self.get_response(request)
