from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from sellers.models import Seller
from basket.models import BasketSale
from . import serializers
from .permissions import IsBuyer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = serializers.SellerSerializer
    permission_classes = (IsAuthenticated, )


class BasketSaleViewSet(viewsets.ModelViewSet):
    queryset = BasketSale.objects.all()
    serializer_class = serializers.BasketSaleSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    def get_queryset(self):
        return BasketSale.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    @list_route(permission_classes=(IsAuthenticated, ))
    def count(self, request, *args, **kwargs):
        count = BasketSale.objects.filter(buyer=self.request.user).count()
        return Response({"count": count})
