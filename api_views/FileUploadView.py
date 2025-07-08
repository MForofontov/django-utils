from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FileUploadView(APIView):
    """
    API view to handle file uploads.
    """

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        """
        Handle POST requests to upload a file.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the file.

        Returns
        -------
        Response
            A JSON response with file information or an error message.
        """
        file = request.FILES.get("file")
        if not file:
            # Return an error response if no file is provided
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Extract file information
        file_info = {
            "filename": file.name,
            "size": file.size,
            "type": file.content_type,
        }

        # Return the file information as a JSON response
        return Response(file_info, status=status.HTTP_200_OK)
