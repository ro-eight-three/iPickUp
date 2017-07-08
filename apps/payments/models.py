from django.db import models


class Payment(models.Model):
    """
    Information about how a buyer payed for an order
    """
    price = models.IntegerField()
