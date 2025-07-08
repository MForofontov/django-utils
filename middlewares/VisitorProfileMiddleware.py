from django.core.cache import cache

class VisitorProfileMiddleware:
    """
    Middleware to track the number of visits to each URL path.
    
    This middleware uses Django's caching framework to count the number of visits
    to each URL path and store the count in the cache.
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
        Handle the incoming request and update the visit count for the URL path.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Generate a cache key based on the request path
        cache_key = f'visits_{request.path}'
        # Get the current visit count from the cache, default to 0 if not present
        visits = cache.get(cache_key, 0)
        # Increment the visit count and store it back in the cache
        cache.set(cache_key, visits + 1, timeout=None)
        # Get the response from the next middleware or view
        response = self.get_response(request)
        return response
