import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FileMetadataView(APIView):
    """
    API view to handle file metadata requests.
    """
    def post(self, request):
        """
        Handle POST requests to retrieve metadata for a specified file.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the file path.

        Returns
        -------
        Response
            A JSON response with the file metadata or an error message.
        """
        file_path = request.data.get('file_path')
        if not file_path or not os.path.isfile(file_path):
            # Return an error response if the file path is invalid or the file does not exist
            return Response({"error": "Invalid file path"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve file statistics
        file_stats = os.stat(file_path)
        metadata = {
            "size": file_stats.st_size,
            "created_at": file_stats.st_ctime,
            "modified_at": file_stats.st_mtime
        }

        # Return the file metadata as a JSON response
        return Response(metadata, status=status.HTTP_200_OK)