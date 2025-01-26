import qrcode
from io import BytesIO
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class QRCodeGeneratorView(APIView):
    """
    API view to handle QR code generation requests.
    """
    def post(self, request):
        """
        Handle POST requests to generate a QR code.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the data to encode in the QR code.

        Returns
        -------
        HttpResponse
            An HTTP response with the generated QR code image or an error message.
        """
        data = request.data.get('data')
        if not data:
            # Return an error response if no data is provided
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the QR code
        qr = qrcode.make(data)
        img_io = BytesIO()
        qr.save(img_io, format='PNG')
        img_io.seek(0)

        # Return the QR code image as an HTTP response
        return HttpResponse(img_io, content_type="image/png")