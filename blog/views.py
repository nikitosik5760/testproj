from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib import messages
from .forms import CommentForm, ArticleForm

# Create your views here.


@login_required()
def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.article = article
            comment.save()
            return redirect('details', slug=slug)
    else:
        form = CommentForm()

    form = CommentForm()

    return render(request, 'blog/details.html', {'article': article, 'form': form})


@login_required()
def random_article(request):
    article = Article.objects.filter(status='active').order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})


def articles_list(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/error_login.html', {'title': "Помилка доступу"})
    articles = Article.objects.filter(status='active')
    return render(request, 'blog/list.html', {'articles': articles, 'title': "Blog - головна сторінка"})


@login_required()
def article_tag_list(request, tag):
    articles = Article.objects.filter(tags__name=tag, status='active')
    return render(request, 'blog/articles_tag_list.html', {'articles': articles, 'title': tag})


@login_required()
def tag_list(request, tag):
    pass


@login_required()
def search(request):
    query = request.GET.get('query', '')

    articles = Article.objects.filter(
        Q(title__icontains=query) | Q(content_preview__icontains=query), status='active')

    return render(request, 'blog/search.html', {'articles': articles, 'title': 'Пошук по сайту', 'query': query})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.add_message(request, messages.INFO,
                                 'Стаття успішно створена')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'blog/create.html', {'form': form, 'title': 'Створення статті'})

    # if request.method == ''


@login_required()
def update(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            article = form.save()
            messages.add_message(
                request, messages.INFO, 'Стаття успішно оновленна')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/update.html', {'form': form, 'title': "Оновлення статті"})


@login_required()
def delete(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.delete()
    messages.add_message(request, messages.INFO,
                         'Стаття успішно видалена')
    return redirect('blog')
