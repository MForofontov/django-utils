import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FileHashingView(APIView):
    """
    API view to handle file hashing requests.
    """
    def post(self, request):
        """
        Handle POST requests to hash a file using a specified hash algorithm.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the file and optional hash algorithm.

        Returns
        -------
        Response
            A JSON response with the file hash or an error message.
        """
        file = request.FILES.get('file')
        hash_algorithm = request.data.get('hash_algorithm', 'sha256')

        if not file:
            # Return an error response if no file is provided
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the hash function from hashlib, default to sha256 if not found
        hash_func = getattr(hashlib, hash_algorithm, hashlib.sha256)
        file_hash = hash_func()
        
        # Read the file in chunks and update the hash
        for chunk in file.chunks():
            file_hash.update(chunk)
        
        # Return the file hash as a JSON response
        return Response({"file_hash": file_hash.hexdigest()}, status=status.HTTP_200_OK)
