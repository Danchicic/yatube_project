from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Create your views here.

def index(request):
    template = "posts/index.html"

    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': "Это главная страница проекта Yatube",
        'posts': posts,

    }

    return render(request, template, context)


def group_posts(request, group_name):
    template = "posts/group_list.html"
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
        'group_name': group_name
    }
    group = get_object_or_404(Group, address=group_name)
    posts = Post.objects.filter(group__address=group_name)
    context['posts'] = posts
    return render(request, template, context)
