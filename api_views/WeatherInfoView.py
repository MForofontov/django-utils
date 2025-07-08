import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WeatherInfoView(APIView):
    """
    API view to handle weather information requests.
    """
    def post(self, request):
        """
        Handle POST requests to fetch weather information for a city.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the city name.

        Returns
        -------
        Response
            A JSON response with weather information or an error message.
        """
        city = request.data.get('city')
        if not city:
            # Return an error response if no city name is provided
            return Response({"error": "City name is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Using OpenWeatherMap API (you need to sign up for an API key)
        api_key = 'your-api-key-here'
        try:
            # Fetch weather information from the external API
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
            response.raise_for_status()
        except requests.RequestException as e:
            # Log the error and return an error response if the request fails
            return Response({"error": "Failed to fetch weather information", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        weather_data = response.json()
        # Return the weather information as a JSON response
        return Response({
            "temperature": weather_data['main']['temp'],
            "humidity": weather_data['main']['humidity'],
            "description": weather_data['weather'][0]['description'],
        }, status=status.HTTP_200_OK)
