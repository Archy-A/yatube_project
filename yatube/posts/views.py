from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug}') 
