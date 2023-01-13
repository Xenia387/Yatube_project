from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    title = 'Yatube. Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Yatube. Сообщество'
    context = {
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
