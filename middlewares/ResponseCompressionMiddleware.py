import gzip
from io import BytesIO


class ResponseCompressionMiddleware:
    """
    Middleware to compress HTTP responses using gzip.

    This middleware compresses the content of HTTP responses with 'text/html' content type
    using gzip to reduce the size of the response.
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
        Handle the incoming request and get the response.

        Parameters
        ----------
        request : HttpRequest
            The incoming HTTP request.

        Returns
        -------
        HttpResponse
            The HTTP response from the next middleware or view.
        """
        # Get the response from the next middleware or view
        response = self.get_response(request)

        # Check if the response content type is 'text/html'
        if response.get(
            "Content-Type"
        ) == "text/html" and "gzip" not in response.get(
            "Content-Encoding", ""
        ):
            # Compress the response content using gzip
            buffer = BytesIO()
            with gzip.GzipFile(fileobj=buffer, mode="wb") as gzip_file:
                gzip_file.write(response.content)
            response.content = buffer.getvalue()
            # Set the 'Content-Encoding' header to 'gzip'
            response["Content-Encoding"] = "gzip"
            # Update the 'Content-Length' header with the length of the compressed content
            response["Content-Length"] = str(len(response.content))

        return response
