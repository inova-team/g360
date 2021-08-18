from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
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
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'categories': categories,

        'title_page': 'Lista de Artículos',
        'is_active_article_list': 'active'
    }
    return render(request, 'article/article_list.html', context)


def article_repository(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    users = User.objects.all()
    media_path = '/media/'
    context = {
        'articles': articles,
        'users': users,
        'categories': categories,
        'media_path': media_path,
        'title_page': 'Lista de Artículos',
        'is_active_article_list': 'active'
    }
    return render(request, 'article/article_repository.html', context)


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
            article.banner.delete()
            article.banner = request.FILES.get('image_uploads')
        if request.FILES.get('pdf_uploads'):
            article.pdf.delete()
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
    print("=======================")
    print(pk)
    print("=======================")
    article = Article.objects.get(pk=pk)
    id_category = article.category_id
    list_articles = Article.objects.filter(category_id=id_category).exclude(pk=pk).order_by('-publication_date')[
                    0:3]

    print("=================================")
    print(article.author_id)
    author = User.objects.get(pk=article.author_id)
    print("===========HOLA========")
    context = {
        'article': article,
        'list_articles': list_articles,
        'author': author,
        'id_category': id_category
    }
    return render(request, "article/article_detail.html", context)


def article_list_search(request, pk):
    articles = Article.objects.filter(category_id=pk).order_by('-publication_date')
    name_categ_article = Article.objects.filter(category_id=pk).values_list('category__name', flat=True)[0]
    context = {
        'articles': articles,
        'name_categ_article': name_categ_article

    }
    return render(request, "article/article_filter.html", context)


def articles_list_category(request):
    id_category = request.POST['category_id']
    id_author= request.POST['author_id']
    filter_text = request.POST['filter_text']
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(request.POST)

    if (id_category == '0'):
        articles = Article.objects.all()
        print("Todos")
    else:
        articles = Article.objects.filter(category_id=id_category).order_by('-publication_date')
        print("por categoria")
    if(id_author != '0'):
        articles = articles.filter(author_id=id_author)
    if(len(filter_text)>0):
        articles = articles.filter(name__contains=filter_text)


    ser_instance = serializers.serialize('json', articles)
    print(ser_instance)

    return JsonResponse({"articles": ser_instance}, status=200)
