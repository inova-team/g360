from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from dictionary.models import Word_Category, Words


def word_upload(request):
    users = User.objects.all()
    categories = Word_Category.objects.all()
    if request.POST:
        word = Words()
        current_userpk = request.user.pk
        user = User.objects.get(pk=current_userpk)
        word.register_author = user
        word.word = request.POST.get('word')
        word.definition = request.POST.get('definition')
        word.save()
        return redirect('word_list')

    context = {
        'users': users,
        'categories': categories,
        'title_page': 'Creación de Palabra',
        'is_active_word_upload': 'active'
    }
    return render(request, 'dictionary/word/word_upload.html', context)


def word_delete(request, pk):
    word = Words.objects.get(pk=pk)
    word.delete()
    return redirect('word_list')


def word_list(request):
    words = Words.objects.all()
    context = {
        'words': words,
        'title_page': 'Lista de Palabras',
        'is_active_word_list': 'active'
    }
    return render(request, 'dictionary/word/word_list.html', context)


def word_update(request, pk):
    word = Words.objects.get(pk=pk)
    users = User.objects.all()
    categories = Word_Category.objects.all()
    if request.POST:

        if request.POST.get('author_select') != "0":
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            word.register_author = author_select

        if request.POST.get('category_select') != "0":
            category_select = Word_Category.objects.get(pk=request.POST.get('category_select'))
            word.category = category_select

        word.word = request.POST.get('word')
        word.definition = request.POST.get('definition')
        word.save()
        return redirect('word_list')

    context = {
        'word': word,
        'users': users,
        'categories': categories,
        'title_page': 'Actualización de Palabra'
    }
    return render(request, 'dictionary/word/word_update.html', context)


def category_upload(request):
    users = User.objects.all()
    categories = Word_Category.objects.all()
    if request.POST:
        category = Word_Category()
        # current_user = request.user
        # category.register_author = current_user
        user = User.objects.get(pk=2)  # el primer usuario
        category.register_author = user
        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')
        category.banner = request.FILES.get('image_uploads')
        category.save()
        return redirect('category_list')

    context = {
        'users': users,
        'categories': categories,
        'title_page': 'Creación de Categoría',
        'is_active_category_upload': 'active'
    }
    return render(request, 'dictionary/category/category_upload.html', context)


def category_delete(request, pk):
    category = Word_Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')


def category_list(request):
    categories = Word_Category.objects.all()
    context = {
        'categories': categories,
        'title_page': 'Lista de Categorías',
        'is_active_category_list': 'active'
    }
    return render(request, 'dictionary/category/category_list.html', context)



def category_update(request, pk):
    users = User.objects.all()
    category = Word_Category.objects.get(pk=pk)
    categories = Word_Category.objects.all()
    if request.POST:
        # current_user = request.user
        # category.update_author = current_user
        user = User.objects.get(pk=2)  # el primer usuario
        category.register_author = user
        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')

        if request.FILES.get('image_uploads'):
            category.banner = request.FILES.get('image_uploads')
        category.save()

        return redirect('category_list')
    context = {
        'category': category,
        'users': users,
        'categories': categories,
        'title_page': 'Actualización de Categoría'
    }

    return render(request, 'dictionary/category/category_update.html', context)

"""
def category_words(request, pk):
    words = Word_Category.objects.filter(category=pk)
    category = Word_Category.objects.get(pk=pk)

    context = {
        'words': words,
        'category': category
    }

    return render(request, 'dictionary/category/category_articles.html', context)
"""
