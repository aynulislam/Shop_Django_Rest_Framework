from django.db import models

# Create your models here.
class SpCategory(models.Model):
    category = models.IntegerField()

    def __str__(self):
        return self.category


class SpSubCategory(models.Model):
    category_id = models.ForeignKey(SpCategory, on_delete=models.CASCADE)
    sub_category = models.ImageField(max_length=100)

    def __str__(self):
        return self.category_id



