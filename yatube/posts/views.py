from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from django.http import HttpResponse

from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    page_title = 'Yatube. Главная страница'
    context = {
        'posts': posts,
        'page_title': page_title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    page_title = f'Yatube. {group.title}'
    context = {
        'group': group,
        'posts': posts,
        'page_title': page_title,
    }
    return render(request, 'posts/group_list.html', context)
