from django.http import HttpResponseForbidden


class IPWhitelistMiddleware:
    """
    Middleware to restrict access based on IP address.

    This middleware allows access only to requests coming from whitelisted IP addresses.
    All other requests will receive a 403 Forbidden response.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable and set the allowed IPs.

        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response
        self.allowed_ips = ["127.0.0.1", "192.168.1.1"]  # Add allowed IPs here

    def __call__(self, request):
        """
        Handle the incoming request and check if the IP address is allowed.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view if the IP is allowed,
            otherwise a 403 Forbidden response.
        """
        # Get the IP address of the request
        ip = request.META.get("REMOTE_ADDR")
        # Check if the IP address is in the allowed list
        if ip not in self.allowed_ips:
            # Return a 403 Forbidden response if the IP is not allowed
            return HttpResponseForbidden("Forbidden")
        # Pass the request to the next middleware or view
        return self.get_response(request)
