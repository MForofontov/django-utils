import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CurrencyConverterView(APIView):
    """
    API view to handle currency conversion requests.
    """
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
        amount = request.data.get('amount')
        from_currency = request.data.get('from_currency')
        to_currency = request.data.get('to_currency')
        
        if not amount or not from_currency or not to_currency:
            # Return an error response if any required parameter is missing
            return Response({"error": "Missing required parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch exchange rates from the external API
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
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