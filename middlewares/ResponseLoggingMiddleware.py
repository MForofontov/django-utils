import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("your_logger_name")

class ResponseLoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log the data being sent to the user in the response.
    """
    def process_response(self, request, response):
        """
        Process the response and log the data being sent to the user.

        Parameters
        ----------
        request : HttpRequest
            The HTTP request object.
        response : HttpResponse
            The HTTP response object.

        Returns
        -------
        HttpResponse
            The HTTP response object.
        """
        # Log the response data
        try:
            # Decode the response content and log it
            response_content = response.content.decode('utf-8')
            logger.info(f"Response data: {response_content}")
        except Exception as e:
            # Log any errors that occur during logging
            logger.error(f"Error logging response data: {e}")

        # Return the response
        return response