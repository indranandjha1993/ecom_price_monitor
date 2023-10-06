from django.db import models
from accounts.models import CustomUser


class Item(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    desired_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    url = models.URLField()
    selector_element = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
