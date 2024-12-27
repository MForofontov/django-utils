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

# Custom view to obtain JWT tokens (access and refresh) and store them in cookies
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to handle obtaining JWT tokens (access and refresh) and storing them in cookies.
    This view extends the TokenObtainPairView from the djangorestframework-simplejwt package.
    """
    # Specify the custom serializer class to use
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
            The HTTP response object containing the new access and refresh tokens in cookies.
        """
        try:
            # Initialize the serializer with the request data
            serializer: CustomTokenObtainPairSerializer = self.get_serializer(data=request.data)
            # Validate the serializer data
            serializer.is_valid(raise_exception=True)
            # Create a response with the validated data
            response: Response = Response(serializer.validated_data)

            # Retrieve the refresh and access tokens from the validated data
            refresh: str = serializer.validated_data['refresh']
            access: str = serializer.validated_data['access']

            # Set the access token in cookies
            response.set_cookie(
                ACCESS_TOKEN_COOKIE_NAME, 
                access, 
                httponly=True, 
                secure=IS_PRODUCTION,  # Set secure based on environment
                samesite='None',
                max_age=ACCESS_TOKEN_MAX_AGE,
            )
            # Set the refresh token in cookies
            response.set_cookie(
                REFRESH_TOKEN_COOKIE_NAME, 
                refresh, 
                httponly=True, 
                secure=IS_PRODUCTION,  # Set secure based on environment
                samesite='None',
                max_age=REFRESH_TOKEN_MAX_AGE,
            )

            # Remove the refresh and access tokens from the response data
            response.data.pop('refresh')
            response.data.pop('access')

            # Log the successful token obtainment
            logger.info('Access and refresh tokens obtained successfully')

            return response

        except Exception as e:
            # Log the error
            logger.error(f'Error obtaining tokens: {str(e)}', exc_info=True)
            # Return an error response if an exception occurs
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
