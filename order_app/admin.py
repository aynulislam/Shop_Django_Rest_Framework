from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import SpOrder,SpOrderDetail

admin.site.register(SpOrder)
admin.site.register(SpOrderDetail)


