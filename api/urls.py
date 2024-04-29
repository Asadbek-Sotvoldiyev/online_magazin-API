from django.urls import path
from .views import (CategoryApiView, CategoryCreateApiView, ProductListCreateApiView,
                    ProductRetrieveUpdateDestroyView, OrderRetrieveUpdateDestroyView, OrderListCreateApiView)


urlpatterns = [
    # category
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:id>/', CategoryApiView.as_view()),
    path('add-category/', CategoryCreateApiView.as_view()),

    # product
    path('product-list-create/', ProductListCreateApiView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),

    # Order
    path('order-list-create/', OrderListCreateApiView.as_view()),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view()),
]