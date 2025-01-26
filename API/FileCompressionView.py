import zipfile
from io import BytesIO
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FileCompressionView(APIView):
    """
    API view to handle file compression requests.
    """
    def post(self, request):
        """
        Handle POST requests to compress a file.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the file to be compressed.

        Returns
        -------
        HttpResponse
            An HTTP response with the compressed file or an error message.
        """
        file = request.FILES.get('file')
        if not file:
            # Return an error response if no file is provided
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a Zip file in memory
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr(file.name, file.read())

        zip_buffer.seek(0)
        # Return the compressed file as an HTTP response
        response = HttpResponse(zip_buffer, content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename={file.name}.zip'
        return response