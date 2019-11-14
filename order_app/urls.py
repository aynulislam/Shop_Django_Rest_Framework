from django.urls import path
from order_app import views
urlpatterns = [
    path('SpOrder/', views.SpOrderAPIView.as_view(), name="sp-order"),
    path('SpOrderDetail/', views.SpOrderDetailAPIView.as_view(), name="sp-delivery-boy"),

    path('sp-order-detail/<int:pk>/', views.SpOrderDetail.as_view()),
    path('je-order-list/', views.SpOrderList.as_view()),
    path('sp-order-detail-detail/<int:pk>/', views.SpOrderDetailDetail.as_view()),
    path('sp-order-detail-list/', views.SpOrderDetailList.as_view()),

]