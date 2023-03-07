from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def categories(request):
    return HttpResponse('<h1>Категории</h1>')
