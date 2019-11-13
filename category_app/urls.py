from django.urls import path
from category_app import views
urlpatterns = [
    path('SpCategory/', views.SpCategoryAPIView.as_view(), name="sp-category"),
    path('SpSubCategory/', views.SpSubCategoryAPIView.as_view(), name="sp-sub-subcategory"),

]