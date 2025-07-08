from django.core.cache import cache
from django.http import HttpResponse


class RateLimitMiddleware:
    """
    Middleware to rate limit incoming requests based on IP address.

    This middleware limits the number of requests a client can make within a specified
    time frame. If the limit is exceeded, a 429 Too Many Requests response is returned.
    """

    def __init__(self, get_response):
        """
        Initialize the middleware with the given get_response callable and set rate limit parameters.

        Parameters
        ----------
        get_response : callable
            The next middleware or view in the chain.
        """
        self.get_response = get_response
        self.rate_limit = 100  # max requests allowed
        self.time_frame = 60  # time frame in seconds

    def __call__(self, request):
        """
        Handle the incoming request and apply rate limiting based on the client's IP address.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view, or a 429 response if the rate limit is exceeded.
        """
        # Get the client's IP address
        ip = request.META.get("REMOTE_ADDR")
        # Generate a cache key based on the IP address
        cache_key = f"rate_limit_{ip}"
        # Get the current request count from the cache
        request_count = cache.get(cache_key, 0)

        # Check if the request count exceeds the rate limit
        if request_count >= self.rate_limit:
            # Return a 429 Too Many Requests response
            return HttpResponse("Too many requests", status=429)

        # Increment the request count and set it in the cache with the specified time frame
        cache.set(cache_key, request_count + 1, self.time_frame)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        return response
