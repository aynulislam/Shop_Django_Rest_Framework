from django.db import models
from seller_app.models import SpDivision
from category_app.models import SpSubCategory


# Create your models here.
class SpGurantee(models.Model):
    gurantee = models.CharField(max_length=100)

    def __str__(self):
        return self.gurantee


class SpProduct(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=100, null=False)
    division_id = models.ForeignKey(SpDivision, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SpSubCategory, on_delete=models.CASCADE)
    description = models.TextField(max_length=100000,null=True)
    password = models.CharField(max_length=255,null=True)
    minimum_qty = models.IntegerField()
    guarantee_id =  models.ForeignKey(SpGurantee, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_code

class SpProductImage(models.Model):
    product_id = models.ForeignKey(SpProduct, on_delete=models.CASCADE)
    image = models.ImageField
    image_path = models.CharField(max_length=100)






