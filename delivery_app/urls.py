from django.urls import path
from delivery_app import views
urlpatterns = [
    path('SpDeliveryOn/', views.SpDeliveryOnAPIView.as_view(), name="sp-delivery-on"),
    path('SpDeliveryBoy/', views.SpDeliveryBoyAPIView.as_view(), name="sp-delivery-boy"),

    path('sp-delivery-on-detail/<int:pk>/', views.SpDeliveryOnDetail.as_view()),
    path('je-delivery-on-list/', views.SpDeliveryOnList.as_view()),
    path('sp-delivery-boy-detail/<int:pk>/', views.SpDeliveryBoyDetail.as_view()),
    path('sp-delivery-boy-list/', views.SpDeliveryBoyList.as_view()),

]