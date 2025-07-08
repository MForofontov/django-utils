import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PasswordStrengthCheckerView(APIView):
    """
    API view to check the strength of a password.
    """

    def post(self, request):
        """
        Handle POST requests to check the strength of a password.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the password.

        Returns
        -------
        Response
            A JSON response with the password strength or an error message.
        """
        password = request.data.get("password")
        if not password:
            # Return an error response if no password is provided
            return Response(
                {"error": "No password provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Determine the strength of the password
        strength = "weak"
        if (
            len(password) >= 8
            and re.search(r"[A-Za-z]", password)
            and re.search(r"\d", password)
        ):
            strength = "medium"
        if (
            len(password) >= 12
            and re.search(r"[A-Za-z]", password)
            and re.search(r"\d", password)
            and re.search(r"[!@#$%^&*()_+]", password)
        ):
            strength = "strong"

        # Return the password strength as a JSON response
        return Response(
            {"password_strength": strength}, status=status.HTTP_200_OK
        )
