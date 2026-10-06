from django.urls import path
from . import views

urlpatterns = [
    path("my_favourite_writer/", views.my_favourite_writer_view),
    path("facts_about_writer/", views.facts_about_writer_view),
    path('my_opinion_about_writer/', views.my_opinion_about_writer_view)

    path('blog_list/', views.blog_list_view),
    path('blog_list/<int:id>/', views.blog_detail_view)
]