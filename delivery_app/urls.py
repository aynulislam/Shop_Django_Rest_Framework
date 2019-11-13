from django.urls import path
from delivery_app import views
urlpatterns = [
    path('SpDeliveryOn/', views.SpDeliveryOnAPIView.as_view(), name="sp-delivery-on"),
    path('SpDeliveryBoy/', views.SpDeliveryBoyAPIView.as_view(), name="sp-delivery-boy"),

]