from django.contrib.gis.geoip2 import GeoIP2

class GeoIPMiddleware:
    """
    Middleware to add GeoIP location data to HTTP requests.
    
    This middleware uses the GeoIP2 library to add location data to each incoming HTTP request
    based on the client's IP address.
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
        Handle the incoming request and add GeoIP location data.
        
        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.
        
        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        geo_ip = GeoIP2()
        # Get the client's IP address, default to localhost if not found
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        try:
            # Get the location data for the IP address
            location = geo_ip.city(ip)
            # Add the location data to the request object
            request.geo_location = location
        except Exception:
            # If an error occurs, set the location data to None
            request.geo_location = None
        # Get the response from the next middleware or view
        return self.get_response(request)
