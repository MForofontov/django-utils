from user_agents import parse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserAgentParserView(APIView):
    """
    API view to parse user-agent strings and extract information about the browser, OS, and device.
    """
    def post(self, request):
        """
        Handle POST requests to parse a user-agent string.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the user-agent string.

        Returns
        -------
        Response
            A JSON response with parsed user-agent information or an error message.
        """
        user_agent = request.data.get('user_agent')
        if not user_agent:
            # Return an error response if no user-agent is provided
            return Response({"error": "No user-agent provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Parse the user-agent string
        ua = parse(user_agent)
        # Return the parsed user-agent information as a JSON response
        return Response({
            "browser": ua.browser.family,
            "browser_version": ua.browser.version_string,
            "os": ua.os.family,
            "os_version": ua.os.version_string,
            "device": ua.device.family,
        }, status=status.HTTP_200_OK)
