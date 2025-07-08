from django.utils import timezone


class CookieConsentMiddleware:
    """
    Middleware to handle cookie consent for users.

    This middleware checks if the 'cookie_consent' cookie is present in the request.
    If not, it sets a default 'cookie_consent' cookie with a value of 'true' and an
    expiration date of one year from the current date.
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
        Handle the incoming request and set the 'cookie_consent' cookie if not present.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response with the 'cookie_consent' cookie set if it was not present.
        """
        # Check if the 'cookie_consent' cookie is present in the request
        consent = request.COOKIES.get("cookie_consent")
        if not consent:
            # Get the response from the next middleware or view
            response = self.get_response(request)
            # Set a default 'cookie_consent' cookie with a value of 'true' and an expiration date of one year
            response.set_cookie(
                "cookie_consent",
                "true",
                expires=timezone.now() + timezone.timedelta(days=365),
            )
            return response
        # Return the response from the next middleware or view if the cookie is already present
        return self.get_response(request)
