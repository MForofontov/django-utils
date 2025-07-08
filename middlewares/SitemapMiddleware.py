from django.urls import get_resolver
from django.http import HttpResponse


class SitemapMiddleware:
    """
    Middleware to generate and serve a sitemap in XML format when a request is made to '/sitemap.xml'.
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
        Handle the incoming request and generate a sitemap if the request path is '/sitemap.xml'.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response containing the sitemap or the response from the next middleware or view.
        """
        if request.path == "/sitemap.xml":
            # Get all named URL patterns
            urls = [
                url.name for url in get_resolver().url_patterns if url.name
            ]
            # Start the sitemap XML
            sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            # Add each URL to the sitemap
            for url in urls:
                sitemap += f"<url><loc>{request.build_absolute_uri(url)}</loc></url>\n"
            # Close the sitemap XML
            sitemap += "</urlset>"
            # Return the sitemap as an XML response
            return HttpResponse(sitemap, content_type="application/xml")
        # Pass the request to the next middleware or view
        return self.get_response(request)
