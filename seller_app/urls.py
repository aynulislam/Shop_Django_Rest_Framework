from django.urls import path
from seller_app import views
urlpatterns = [
    path('ScUser/', views.ScUserAPIView.as_view(), name="sc-user"),
    path('SpSeller/', views.SpSellerAPIView.as_view(), name="sp-seller"),
    path('SpDivision/', views.SpDivisionAPIView.as_view(), name="sp-division"),

]