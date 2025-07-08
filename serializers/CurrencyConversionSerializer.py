from rest_framework import serializers


class CurrencyConversionSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
