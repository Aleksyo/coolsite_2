from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи {post_id}')


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
