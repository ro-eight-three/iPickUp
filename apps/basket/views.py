from django.views.generic import View
from django.shortcuts import render
from sellers.models import Seller
from .models import BasketSale


class BasketListView(View):
    def get(self, request, *args, **kwargs):

        buyer = request.user
        sellers = Seller.objects.filter(
            product__basketsale__buyer=buyer).distinct()

        basketsales_by_seller = []
        for seller in sellers:
            basketsales_by_seller.append(
                BasketSale.objects.filter(buyer=buyer, product__seller=seller))

        return render(request, "basket/basketsale_list.html",
                      {"basketsales_by_seller": basketsales_by_seller})
