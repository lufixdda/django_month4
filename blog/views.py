from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from django.db.models import F

from django.views import generic

class SearchView(generic.ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blog'
    model = models.Blog

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return self.model.objects.filter(title__icontains=q)
        return self.model.objects.all()


class BookSearchView(generic.ListView):
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return self.model.objects.filter(title__icontains=q)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



class BookListView(ListView):
    model = models.Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = 2
    


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        viewed_books = request.session.get('viewed_books', [])

        if obj.pk not in viewed_books:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            viewed_books.append(obj.pk)
            request.session['viewed_books'] = viewed_books
            obj.refresh_from_db()
        return obj


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
