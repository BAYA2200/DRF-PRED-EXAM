from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('api/shop/category/', views.CategoryListCreateAPIView.as_view()),
    path('api/shop/category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/shop/category/<int:pk>/item/', views.ItemListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:pk>/order/',views.OrderCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:item_id>/order/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view())


]
