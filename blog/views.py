from django.shortcuts import render
from django.http import HttpResponse


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