from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

# Create your views here.


def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'title': found_post['title'] + ' - ',
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def exemplo(request):
    print('blog')

    context = {
        'text': 'Olá exemplo',
        'title': 'Exemplo - '
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
