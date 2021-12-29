from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Post, Group

# Главная страница
#def index(request):    
#    template = loader.get_template('posts/index.html')
#    title = "Это главная страница проекта Yatube"
#    context = {
#        'title': title
#              }
#    return HttpResponse(template.render(context, request)) 

def index(request):
    title = "Это главная страница проекта Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = group.title
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context) 

# view-функция принимает параметр pk из path()
#def group_posts(request, slug):
#    template = loader.get_template('posts/group_list.html')

#    group = get_object_or_404(Group, slug=slug)

#    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
#    context = {
#        'group': group,
#        'posts': posts,
#    }
#    return HttpResponse(template.render(context, request)) 









    