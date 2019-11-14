from django.urls import path
from category_app import views
urlpatterns = [
    path('SpCategory/', views.SpCategoryAPIView.as_view(), name="sp-category"),
    path('SpSubCategory/', views.SpSubCategoryAPIView.as_view(), name="sp-sub-subcategory"),

    path('sp-category-detail/<int:pk>/', views.SpCategoryDetail.as_view()),
    path('je-category-list/', views.SpCategoryList.as_view()),
    path('sp-subcategory-detail/<int:pk>/', views.SpSubCategoryDetail.as_view()),
    path('sp-subcategory-list/', views.SpSubCategoryList.as_view()),
]