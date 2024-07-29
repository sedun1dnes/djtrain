from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Войти", 'url_name': 'login'}]

ds_list = [
    {'id': 1, 'name': 'Очередь'},
    {'id': 2, 'name': 'Стэк'},
    {'id': 3, 'name': 'Дэк'},
    {'id': 4, 'name': 'Куча'},
]
data_db = [
    {'name': 'brestprog', 'description': 'Хорошо написанные статьи по методам и структурам данных',
     'url': 'https://brestprog.by/topics/'},
    {'name': 'Data Structure Visualizations', 'description': 'Визуализатор работы некоторых алгоритмов и СД',
     'url': 'https://www.cs.usfca.edu/~galles/visualization/Algorithms.html'},
    {'name': 'School of Information Technologies and Engineering data', 'description': 'Курсы, решение задач e-olimp',
     'url': 'https://site.ada.edu.az/~medv/'},
]


def structures(request):
    data = {
        'title': 'Структуры данных',
        'menu': menu,
        'ds_list': ds_list,
        'interesting_sites': data_db,
    }
    return render(request, 'datastructures/home.html', data)


def datastructure(request, num):
    if num > 100:
        raise Http404()
    if num > 10:
        return redirect('home')
    return HttpResponse(f'datastructure #{num}')


def add_page(request):
    data = {
        'title': 'Новая страница',
        'menu': menu,
    }
    return render(request, 'datastructures/add_page.html', data)


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
