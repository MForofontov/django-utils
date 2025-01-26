import ipaddress
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IPValidatorView(APIView):
    """
    API view to validate IP addresses.
    """
    def post(self, request):
        """
        Handle POST requests to validate an IP address.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the IP address.

        Returns
        -------
        Response
            A JSON response indicating whether the IP address is valid or not.
        """
        ip = request.data.get('ip')
        if not ip:
            # Return an error response if no IP address is provided
            return Response({"error": "No IP provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate the IP address
            ipaddress.ip_address(ip)
            return Response({"is_valid": True}, status=status.HTTP_200_OK)
        except ValueError:
            # Return a response indicating the IP address is invalid
            return Response({"is_valid": False}, status=status.HTTP_200_OK)