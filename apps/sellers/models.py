from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    presentation_name = models.CharField(max_length=100)
    administrative_name = models.CharField(max_length=100)

    def __str__(self):
        return "Seller {}".format(self.user.first_name)
