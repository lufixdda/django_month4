from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list,),
    path('product_list/<int:id>/', views.product_detail,),
]