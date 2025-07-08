from cryptography.fernet import Fernet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataEncryptionView(APIView):
    """
    API view to handle data encryption and decryption requests.
    """
    def post(self, request):
        """
        Handle POST requests to encrypt or decrypt data.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the action, data, and key.

        Returns
        -------
        Response
            A JSON response with the encrypted or decrypted data, or an error message.
        """
        action = request.data.get('action')
        data = request.data.get('data')
        key = request.data.get('key')

        if not data or not key or not action:
            # Return an error response if any required field is missing
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fernet = Fernet(key)
        except Exception as e:
            # Return an error response if the key is invalid
            return Response({"error": f"Invalid key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        if action == 'encrypt':
            try:
                encrypted_data = fernet.encrypt(data.encode())
                return Response({"encrypted_data": encrypted_data.decode()}, status=status.HTTP_200_OK)
            except Exception as e:
                # Return an error response if encryption fails
                return Response({"error": f"Encryption failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        elif action == 'decrypt':
            try:
                decrypted_data = fernet.decrypt(data.encode()).decode()
                return Response({"decrypted_data": decrypted_data}, status=status.HTTP_200_OK)
            except Exception as e:
                # Return an error response if decryption fails
                return Response({"error": f"Decryption failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response if the action is invalid
            return Response({"error": "Invalid action. Use 'encrypt' or 'decrypt'"}, status=status.HTTP_400_BAD_REQUEST)
