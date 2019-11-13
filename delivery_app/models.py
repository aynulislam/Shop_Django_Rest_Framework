from django.db import models
from seller_app.models import SpSeller
from purchase_app.models import SpPurchase
# Create your models here.
class SpDeliveryBoy(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=255)
    seller_id = models.ForeignKey(SpSeller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SpDeliveryOn(models.Model):
    purchase_id = models.ForeignKey(SpPurchase, on_delete=models.CASCADE)
    delivery_boy_id = models.ForeignKey(SpDeliveryBoy, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=255)
    long_start = models.DecimalField(max_digits=10, decimal_places=3)
    lat_start = models.DecimalField(max_digits=10, decimal_places=3)
    long_end = models.DecimalField(max_digits=10, decimal_places=3)
    lat_end = models.DecimalField(max_digits=10, decimal_places=3)

    delivery_date = models.DateTimeField

    def __str__(self):
        return self.purchase_id