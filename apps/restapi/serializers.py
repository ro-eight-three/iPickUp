from rest_framework import serializers
from sellers.models import Seller
from basket.models import BasketSale


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'info', 'address', 'presentation_name',
                  'administrative_name')


class BasketSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketSale
        fields = ('id', 'product', 'quantity', 'comment')
