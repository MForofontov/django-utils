import requests

class WeatherInfoView(APIView):
    def post(self, request):
        city = request.data.get('city')
        if not city:
            return Response({"error": "City name is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Using OpenWeatherMap API (you need to sign up for an API key)
        api_key = 'your-api-key-here'
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        if response.status_code == 200:
            weather_data = response.json()
            return Response({
                "temperature": weather_data['main']['temp'],
                "humidity": weather_data['main']['humidity'],
                "description": weather_data['weather'][0]['description'],
            }, status=status.HTTP_200_OK)
        return Response({"error": "City not found"}, status=status.HTTP_400_BAD_REQUEST)
