from django.urls import path
from product_app import views
urlpatterns = [
    path('SpGurantee/', views.SpGuranteeAPIView.as_view(), name="sp-gurantee"),
    path('SpProduct/', views.SpProductAPIView.as_view(), name="sp-product"),
    path('SpProductImage/', views.SpProductImageAPIView.as_view(), name="sp-product-image"),

]