from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'sellers', viewsets.SellerViewSet)
router.register(r'basket', viewsets.BasketSaleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
