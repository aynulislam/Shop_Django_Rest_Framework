from django.urls import path
from product_app import views
urlpatterns = [
    path('SpGurantee/', views.SpGuranteeAPIView.as_view(), name="sp-gurantee"),
    path('SpProduct/', views.SpProductAPIView.as_view(), name="sp-product"),
    path('SpProductImage/', views.SpProductImageAPIView.as_view(), name="sp-product-image"),

    path('sp-gurantee-detail/<int:pk>/', views.SpGuranteeDetail.as_view()),
    path('sp-gurantee-list/', views.SpGuranteeList.as_view()),
    path('sp-product-detail/<int:pk>/', views.SpProductDetail.as_view()),
    path('sp-order-detail-list/', views.SpProductList.as_view()),
    path('sp-product-image-detail/<int:pk>/', views.SpProductImageDetail.as_view()),
    path('sp-product-image-list/', views.SpProductImageList.as_view()),

]