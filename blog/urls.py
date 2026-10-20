from django.urls import path
from . import views

urlpatterns = [
    path("my_favourite_writer/", views.FavouriteWriterView.as_view()),
    path("facts_about_writer/", views.FactsAboutWriterView.as_view()),
    path('my_opinion_about_writer/', views.OpinionAboutWriterView.as_view()),

    path('blog_list/', views.BlogListView.as_view()),
    path('blog_list/<int:pk>/', views.BlogDetailView.as_view())
]
