from datetime import datetime
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TimeZoneConverterView(APIView):
    """
    API view to handle time zone conversion requests.
    """
    def post(self, request):
        """
        Handle POST requests to convert a time from one time zone to another.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the time, source time zone, and target time zone.

        Returns
        -------
        Response
            A JSON response with the converted time or an error message.
        """
        time_str = request.data.get('time')
        source_tz = request.data.get('source_timezone')
        target_tz = request.data.get('target_timezone')

        if not time_str or not source_tz or not target_tz:
            # Return an error response if any required parameter is missing
            return Response({"error": "Missing required parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert the time from the source time zone to the target time zone
            source_timezone = pytz.timezone(source_tz)
            target_timezone = pytz.timezone(target_tz)
            source_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            source_time = source_timezone.localize(source_time)
            target_time = source_time.astimezone(target_timezone)
            # Return the converted time as a JSON response
            return Response({"converted_time": target_time.strftime('%Y-%m-%d %H:%M:%S')}, status=status.HTTP_200_OK)
        except Exception as e:
            # Return an error response if the conversion fails
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
