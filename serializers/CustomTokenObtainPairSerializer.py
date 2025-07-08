from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Type, Any


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer to handle obtaining JWT tokens (access and refresh).
    This serializer extends the TokenObtainPairSerializer from the djangorestframework-simplejwt package.
    """

    @classmethod
    def get_token(
        cls: Type[TokenObtainPairSerializer], user: Any
    ) -> RefreshToken:
        """
        Generate a refresh token for the given user.

        Args:
            cls (Type[TokenObtainPairSerializer]): The class type.
            user (Any): The user for whom to generate the token.

        Returns:
            RefreshToken: The generated refresh token.
        """
        # Call the parent class's get_token method to get the default token
        token = super().get_token(user)

        # Add custom claims here if needed

        return token
