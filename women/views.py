from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Категории</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2020:
        # raise Http404() # исключение 404
        return redirect('home', permanent=True)  # 302 постоянный, 301 временный
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
