from django.urls import path
from seller_app import views
urlpatterns = [
    path('ScUser/', views.ScUserAPIView.as_view(), name="sc-user"),
    path('SpSeller/', views.SpSellerAPIView.as_view(), name="sp-seller"),
    path('SpDivision/', views.SpDivisionAPIView.as_view(), name="sp-division"),

    path('sc-user-detail/<int:pk>/', views.ScUserDetail.as_view()),
    path('sc-user-list/', views.ScUserList.as_view()),
    path('sp-seller-detail/<int:pk>/', views.SpSellerDetail.as_view()),
    path('sp-wbcard-list/', views.SpSellerList.as_view()),
    path('sp-division-detail/<int:pk>/', views.SpDivisionDetail.as_view()),
    path('sp-division-list/', views.SpDivisionList.as_view()),
]