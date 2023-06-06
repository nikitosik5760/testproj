from django.shortcuts import render
from blog.models import Article
# Create your views here.


def frontpage(request):
    articles = Article.objects.all()
    return render(request, 'core/frontpage.html', {'title': 'Головна Сторінка', 'articles': articles})


def about(request):
    return render(request, 'core/about.html', {'title': 'O нас'})
