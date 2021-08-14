from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article
from .models import Category
from django.contrib.auth.models import User


def article_upload(request):
    users = User.objects.all()
    categories = Category.objects.all()
    if request.POST:
        article = Article()

        if request.POST.get('author_select') != "0":
            print("===========================")
            print(request.POST.get('author_select'))
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            article.author = author_select

        if request.POST.get('category_select') != "0":
            category_select = Category.objects.get(pk=request.POST.get('category_select'))
            article.category = category_select

        article.name = request.POST.get('name')
        article.description = request.POST.get('description')
        article.banner = request.FILES.get('image_uploads')
        article.pdf = request.FILES.get('pdf_uploads')
        article.save()
        return redirect('article_list')

    context = {
        'users': users,
        'categories': categories,
        'title_page': 'Creación de Artículo',
        'is_active_article_upload': 'active'
    }
    return render(request, 'article/article_upload.html', context)


def article_delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article_list')


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title_page': 'Lista de Artículos',
        'is_active_article_list': 'active'
    }
    return render(request, 'article/article_list.html', context)


def article_update(request, pk):
    users = User.objects.all()
    article = Article.objects.get(pk=pk)
    categories = Category.objects.all()
    if request.POST:

        if request.POST.get('author_select') != "0":
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            article.author = author_select

        if request.POST.get('category_select') != "0":
            category_select = Category.objects.get(pk=request.POST.get('category_select'))
            article.category = category_select

        article.name = request.POST.get('name')
        article.description = request.POST.get('description')

        if request.FILES.get('image_uploads'):
            article.banner = request.FILES.get('image_uploads')
        if request.FILES.get('pdf_uploads'):
            article.pdf = request.FILES.get('pdf_uploads')
        article.save()

        return redirect('article_list')
    context = {
        'article': article,
        'users': users,
        'categories': categories,
        'title_page': 'Actualización de Artículo'
    }
    return render(request, 'article/article_update.html', context)


def article_detail(request, pk):
    article = Article.objects.filter(pk=pk).exists()
    if article:
        article = Article.objects.get(pk=pk)
        id_category = article.category_id
        list_articles = Article.objects.filter(category_id=id_category).exclude(pk=pk).order_by('-publication_date')[
                        0:3]
        author = User.objects.get(username=article.author.user)
        context = {
            'article': article,
            'list_articles': list_articles,
            'author': author,
            'id_category': id_category
        }
        return render(request, "article/article_detail.html", context)
    else:
        return redirect('home')


def article_list_search(request, pk):
    articles = Article.objects.filter(category_id=pk).order_by('-publication_date')
    name_categ_article = Article.objects.filter(category_id=pk).values_list('category__name', flat=True)[0]
    context = {
        'articles': articles,
        'name_categ_article': name_categ_article

    }
    return render(request, "article/article_filter.html", context)