from django.db import models
from sellers.models import Seller


class Product(models.Model):
    """
    A Product that is sold by a Seller and can be bougth by a Buyer
    """
    seller = models.ForeignKey(Seller)
    name = models.CharField(max_length=100)
    descirption = models.CharField(max_length=300)
    preparation_time = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.name
