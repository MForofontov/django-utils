import requests

class IPGeolocationView(APIView):
    def post(self, request):
        ip_address = request.data.get('ip', '')
        if not ip_address:
            return Response({"error": "No IP address provided"}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"error": "Could not fetch geolocation"}, status=status.HTTP_400_BAD_REQUEST)
