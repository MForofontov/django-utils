import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmailValidatorView(APIView):
    """
    API view to validate email addresses.
    """

    def post(self, request):
        """
        Handle POST requests to validate an email address.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the email address.

        Returns
        -------
        Response
            A JSON response indicating whether the email address is valid or not.
        """
        email = request.data.get("email")
        if not email:
            # Return an error response if no email is provided
            return Response(
                {"error": "No email provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Regular expression for validating an email address
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        is_valid = bool(re.match(email_regex, email))

        # Return the validation result as a JSON response
        return Response({"is_valid": is_valid}, status=status.HTTP_200_OK)
