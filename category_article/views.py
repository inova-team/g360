from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category
from authentication.models import User
from article.models import Article


def category_upload(request):
    users = User.objects.all()
    categories = Category.objects.all()
    if request.POST:
        category = Category()

        if request.POST.get('responsable_select') != "0":
            responsable_select = User.objects.get(pk=request.POST.get('responsable_select'))
            category.responsable = responsable_select

        if request.POST.get('category_select') != "0":
            category_select = Category.objects.get(pk=request.POST.get('category_select'))
            category.category_father = category_select
            category.has_father = True

        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')
        category.banner = request.FILES.get('image_uploads')
        category.save()
        return redirect('category_article_list')

    context = {
        'users': users,
        'categories': categories,
        'title_page': 'Creación de Categoría',
        'is_active_category_article_upload': 'active'
    }
    return render(request, 'category_article/category_upload.html', context)


def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title_page': 'Lista de Categorías',
        'is_active_category_article_list': 'active'
    }
    return render(request, 'category_article/category_list_intranet.html', context)


def category_update(request, pk):
    users = User.objects.all()
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    if request.POST:

        if request.POST.get('responsable_select') != "0":
            responsable_select = User.objects.get(pk=request.POST.get('responsable_select'))
            category.responsable = responsable_select

        if request.POST.get('category_select') != "0":
            category_select = Category.objects.get(pk=request.POST.get('category_select'))
            category.category_father = category_select
            category.has_father = True
        else:
            category.category_father = None
            category.has_father = False

        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')

        if request.FILES.get('image_uploads'):
            category.banner = request.FILES.get('image_uploads')
        category.save()

        return redirect('category_article_list')
    context = {
        'category': category,
        'users': users,
        'categories': categories,
        'title_page': 'Actualización de Categoría'
    }

    return render(request, 'category_article/category_update.html', context)


def category_articles(request, pk):
    articles = Article.objects.filter(category=pk)
    category = Category.objects.get(pk=pk)

    context = {
        'articles': articles,
        'category': category
    }

    return render(request, 'category_article/category_articles.html', context)