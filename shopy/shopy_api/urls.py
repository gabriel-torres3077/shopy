from django.contrib import admin
from django.urls import path, include
from .views import ProductViewSet, OrderViewSet, OrderDetail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', ProductViewSet.as_view()),
    path('orders/', OrderViewSet.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view())
]