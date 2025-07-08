import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IPGeolocationView(APIView):
    """
    API view to handle IP geolocation requests.
    """
    def post(self, request):
        """
        Handle POST requests to fetch geolocation information for an IP address.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the IP address.

        Returns
        -------
        Response
            A JSON response with geolocation information or an error message.
        """
        ip_address = request.data.get('ip', '')
        if not ip_address:
            # Return an error response if no IP address is provided
            return Response({"error": "No IP address provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch geolocation information from the external API
            response = requests.get(f'https://ipinfo.io/{ip_address}/json')
            response.raise_for_status()
        except requests.RequestException as e:
            # Log the error and return an error response if the request fails
            return Response({"error": "Could not fetch geolocation", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Return the geolocation information as a JSON response
        return Response(response.json(), status=status.HTTP_200_OK)
