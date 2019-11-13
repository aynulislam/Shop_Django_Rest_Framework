from django.urls import path
from purchase_app import views
urlpatterns = [
    path('WbCard/', views.WbCardAPIView.as_view(), name="wb-card"),
    path('SpPurchase/', views.SpPurchaseAPIView.as_view(), name="sp-purchase"),

]