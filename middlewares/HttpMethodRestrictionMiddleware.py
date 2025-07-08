from django.http import HttpResponseNotAllowed


class HttpMethodRestrictionMiddleware:
    """
    Middleware to restrict HTTP methods for specific paths.

    This middleware restricts certain HTTP methods (e.g., POST, DELETE) for specific
    paths in the application. If a restricted method is used, a 405 Method Not Allowed
    response is returned.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable and set restricted paths.

        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response
        # Define paths and their restricted methods
        self.restricted_paths = {
            "/admin/sensitive-endpoint/": ["POST", "DELETE"],
        }

    def __call__(self, request):
        """
        Handle the incoming request and restrict HTTP methods for specific paths.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view, or a 405 response if the method is restricted.
        """
        # Check if the request path and method are restricted
        for path, methods in self.restricted_paths.items():
            if request.path.startswith(path) and request.method in methods:
                # Return a 405 Method Not Allowed response if the method is restricted
                return HttpResponseNotAllowed(permitted_methods=["GET"])
        # Pass the request to the next middleware or view
        return self.get_response(request)
