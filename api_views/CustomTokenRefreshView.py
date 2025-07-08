import logging
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.request import Request
from serializers.CustomTokenRefreshSerializer import CustomTokenRefreshSerializer
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

class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom view to handle refreshing JWT tokens and storing them in cookies.
    This view extends the TokenRefreshView from the djangorestframework-simplejwt package.
    """
    serializer_class = CustomTokenRefreshSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Handle POST requests to refresh JWT tokens.

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
            A JSON response with the refreshed JWT tokens or an error message.
        """
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

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
        if tokens.get('refresh'):
            response.set_cookie(
                REFRESH_TOKEN_COOKIE_NAME,
                tokens['refresh'],
                max_age=REFRESH_TOKEN_MAX_AGE,
                httponly=True,
                secure=IS_PRODUCTION,
                samesite='Strict' if IS_PRODUCTION else 'Lax'
            )

        return response
