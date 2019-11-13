from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import WbCard,SpPurchase

admin.site.register(WbCard)
admin.site.register(SpPurchase)
