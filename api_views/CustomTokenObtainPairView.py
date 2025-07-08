import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.request import Request
from serializers.CustomTokenObtainPairSerializer import CustomTokenObtainPairSerializer
from typing import Any
import os

# Initialize logger
logger = logging.getLogger(__name__)

# Constants for cookie names and max age values
ACCESS_TOKEN_COOKIE_NAME: str = 'accessToken'
REFRESH_TOKEN_COOKIE_NAME: str = 'refreshToken'
ACCESS_TOKEN_MAX_AGE: int = 3600  # 1 hour
REFRESH_TOKEN_MAX_AGE: int = 3600 * 24  # 1 day

# Determine if the environment is production
IS_PRODUCTION: bool = os.getenv('DJANGO_ENV') == 'production'

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to handle obtaining JWT tokens (access and refresh) and storing them in cookies.
    This view extends the TokenObtainPairView from the djangorestframework-simplejwt package.
    """
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Handle POST requests to obtain JWT tokens.

        Parameters
        ----------
        request : Request
            The HTTP request object.
        *args : Any
            Additional positional arguments.
        **kwargs : Any
            Additional keyword arguments.

        Returns
        -------
        Response
            A JSON response with the JWT tokens or an error message.
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            logger.error(f"Token obtain failed: {e}")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Get the validated data (tokens)
        tokens = serializer.validated_data

        # Create the response object
        response = Response(tokens, status=status.HTTP_200_OK)

        # Set the cookies for access and refresh tokens
        response.set_cookie(
            ACCESS_TOKEN_COOKIE_NAME,
            tokens['access'],
            max_age=ACCESS_TOKEN_MAX_AGE,
            httponly=True,
            secure=IS_PRODUCTION,
            samesite='Strict' if IS_PRODUCTION else 'Lax'
        )
        response.set_cookie(
            REFRESH_TOKEN_COOKIE_NAME,
            tokens['refresh'],
            max_age=REFRESH_TOKEN_MAX_AGE,
            httponly=True,
            secure=IS_PRODUCTION,
            samesite='Strict' if IS_PRODUCTION else 'Lax'
        )

        return response
