from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def blog_list_view(request):
    if request.method == 'GET':
        blog = models.Blog.objects.all()
    return render(request, 'blog_list.html', {'blog': blog})


def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})













def my_favourite_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('мне нравится трилогия Гарии Потера так что Джоан Роулинг')


def facts_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse('Джоан Роулинг написала первую книгу, которая называется «Гарри Поттер и философский камень», в период с 1990 по 1995 год')


def my_opinion_about_writer_view(request):
    if request.method == 'GET':
        return HttpResponse(
            "Джоан Роулинг — всемирно известная писательница, "
            "создавшая легендарную вселенную Гарри Поттера и "
            "вдохновляющая многих своей благотворительностью, "
            "но в последние годы вызывающая острые общественные споры "
            "из-за своих бескомпромиссных политических и социальных взглядов."
        )