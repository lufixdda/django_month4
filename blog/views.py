from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from . import models


class BookListView(ListView):
    model = models.Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BlogListView(ListView):
    model = models.Blog
    template_name = 'blog_list.html'
    context_object_name = 'blog'


class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog_id'


class FavouriteWriterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('мне нравится трилогия Гарии Потера так что Джоан Роулинг')


class FactsAboutWriterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Джоан Роулинг написала первую книгу, которая называется «Гарри Поттер и философский камень», в период с 1990 по 1995 год')


class OpinionAboutWriterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(
            "Джоан Роулинг — всемирно известная писательница, "
            "создавшая легендарную вселенную Гарри Поттера и "
            "вдохновляющая многих своей благотворительностью, "
            "но в последние годы вызывающая острые общественные споры "
            "из-за своих бескомпромиссных политических и социальных взглядов."
        )
