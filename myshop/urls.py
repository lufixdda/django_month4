from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view()),
    path('product_list/<int:pk>/', views.ProductDetailView.as_view()),
]
