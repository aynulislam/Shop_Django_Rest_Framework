from django.db import models
from order_app.models import SpOrder
from seller_app.models import ScUser

# Create your models here.
class WbCard(models.Model):
    card_no = models.CharField(max_length=15,null=False)
    password = models.CharField(max_length=15,null=False)
    salt = models.IntegerField()
    user_id = models.ForeignKey(ScUser, on_delete=models.CASCADE)
    pp_no = models.CharField(max_length=20)
    nid_no = models.IntegerField()


    def __str__(self):
        return self.card_no


class SpPurchase(models.Model):
    order_id = models.ForeignKey(SpOrder, on_delete=models.CASCADE)
    card_id = models.ForeignKey(WbCard, on_delete=models.CASCADE)
    total_amt = models.DecimalField(max_digits=20, decimal_places=2)
    pay_status = models.IntegerField()
    delivery_status =  models.IntegerField()
    user_status =  models.IntegerField()

    def __str__(self):
        return self.order_id


