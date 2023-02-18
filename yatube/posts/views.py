from django.shortcuts import get_object_or_404, render

from .models import Group, Post

SLICE = 10

def index(request):
    posts = Post.objects.all()[:SLICE]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:SLICE]
    title = (f'Записи сообщества {group.title}')
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
