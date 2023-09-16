from django.shortcuts import render

# Create your views here.


def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog'
    }

    return render(
        request,
        'blog/index.html',
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
