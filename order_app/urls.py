from django.urls import path
from order_app import views
urlpatterns = [
    path('SpOrder/', views.SpOrderAPIView.as_view(), name="sp-order"),
    path('SpOrderDetail/', views.SpOrderDetailAPIView.as_view(), name="sp-delivery-boy"),

]