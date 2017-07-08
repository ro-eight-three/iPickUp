from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class AbstractSale(models.Model):
    """
    Contains fields shared between BasketSale and FinalizedSale
    """

    class Meta:
        abstract = True

    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{} {}".format(self.product.name, self.quantity)


class BasketSale(AbstractSale):
    """
    A sale that is only in the shopping basket of a buyer and
    not yet finalized, payed for
    """
    buyer = models.ForeignKey(User)
