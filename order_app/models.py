from django.db import models
from seller_app.models import ScUser
from product_app.models import SpProduct

# Create your models here.

class SpOrder(models.Model):
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=255)
    longtitude = models.IntegerField()
    latitude =  models.IntegerField()
    #longitude = models.DecimalField(max_digits=10, decimal_places=3)
    #latitude = models.DecimalField(max_digits=10, decimal_places=3)
    ship_charge = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.user_id

class SpOrderDetail(models.Model):
    order_id = models.ForeignKey(SpOrder, on_delete=models.CASCADE)
    product_id = models.ForeignKey(SpProduct, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    qty = models.IntegerField()


    def __str__(self):
        return self.order_id
