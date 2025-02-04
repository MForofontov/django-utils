from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers.CurrencyConversionSerializer import CurrencyConversionSerializer
import requests

class CurrencyConverterView(APIView):
    """
    API view to handle currency conversion requests.
    """
    EXCHANGE_RATE_API_URL = 'https://api.exchangerate-api.com/v4/latest/'

    def post(self, request):
        """
        Handle POST requests to convert an amount from one currency to another.

        Parameters
        ----------
        request : Request
            The HTTP request object containing the amount, from_currency, and to_currency.

        Returns
        -------
        Response
            A JSON response with the converted amount or an error message.
        """
        serializer = CurrencyConversionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']
            
            try:
                # Fetch exchange rates from the external API
                response = requests.get(f'{self.EXCHANGE_RATE_API_URL}{from_currency}')
                response.raise_for_status()
            except requests.RequestException as e:
                # Log the error and return an error response if the request fails
                return Response({"error": "Failed to fetch exchange rates", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            data = response.json()
            exchange_rate = data['rates'].get(to_currency)
            if exchange_rate:
                # Calculate the converted amount
                converted_amount = float(amount) * exchange_rate
                return Response({"converted_amount": converted_amount}, status=status.HTTP_200_OK)
            
            # Return an error response if the target currency is invalid
            return Response({"error": "Invalid target currency"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return an error response if the input data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)