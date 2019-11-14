from django.urls import path
from purchase_app import views
urlpatterns = [
    path('WbCard/', views.WbCardAPIView.as_view(), name="wb-card"),
    path('SpPurchase/', views.SpPurchaseAPIView.as_view(), name="sp-purchase"),

    path('sp-purchase-detail/<int:pk>/', views.SpPurchaseDetail.as_view()),
    path('sp-purchase-list/', views.SpPurchaseList.as_view()),
    path('sp-wbcard-detail/<int:pk>/', views.WbCardDetail.as_view()),
    path('sp-wbcard-list/', views.WbCardList.as_view()),

]