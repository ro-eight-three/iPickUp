from django.db import models
from django.contrib.auth.models import User
from basket.models import AbstractSale
from payments.models import Payment
from products.models import Product
from sellers.models import Seller


class Order(models.Model):
    """
    A list of products that a Buyer has FinalizedSales for
    """
    buyer = models.ForeignKey(User)
    payment = models.ForeignKey(Payment)
    ordered_time = models.DateTimeField()

    def __str__(self):
        return "Order {} for {}".format(self.id, self.buyer.user.first_name)


class PickPackage(models.Model):
    """
    Every order has one or more PickPackages when it's finalized.
    Depending on how the products can be packaged: from differen sellers,
    with different pickup times
    """
    order = models.ForeignKey(Order)
    pickup_time = models.DateTimeField()
    seller = models.ForeignKey(Seller)


class FinalizedSale(AbstractSale):
    """
    A product that is part of an Order the Buyer has finalized and will be
    in a specific PickPackage
    """
    package = models.ForeignKey(PickPackage)
    payed_price = models.IntegerField()
    # product might have been changed since sale,
    # so we backup at least the name
    product_name = models.CharField(max_length=100)
