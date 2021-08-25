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

        if request.POST.get('category_select') != "0":
            category_select = Word_Category.objects.get(pk=request.POST.get('category_select'))
            word.category = category_select

        word.word = request.POST.get('word')
        word.definition = request.POST.get('definition')

        show_word_user = request.POST.get('show_word_user')
        if (show_word_user == 'on'):
            word.show_user = True
        else:
            word.show_user = False

        word.save()
        return redirect('word_list_intranet')

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
    return redirect('word_list_intranet')


def word_list(request, pk):
    category = Word_Category.objects.get(pk=pk)
    words = Words.objects.filter(category_id=category.pk, show_user=True)
    media_path = '/media/'
    context = {
        'words': words,
        'category': category,
        'media_path': media_path,
        'title_page': 'Lista de palabras de la categoría',
        'is_active_word_list': 'active'
    }
    return render(request, 'dictionary/word/word_list.html', context)


def word_list_intranet(request):
    words = Words.objects.all()
    context = {
        'words': words,
        'title_page': 'Lista de Palabras',
        'is_active_word_list': 'active'
    }
    return render(request, 'dictionary/word/word_list_intranet.html', context)


def word_update(request, pk):
    word = Words.objects.get(pk=pk)
    users = User.objects.all()
    categories = Word_Category.objects.all()
    if request.POST:
        current_userpk = request.user.pk
        user = User.objects.get(pk=current_userpk)
        word.register_author = user

        if request.POST.get('category_select') != "0":
            category_select = Word_Category.objects.get(pk=request.POST.get('category_select'))
            word.category = category_select

        word.word = request.POST.get('word')
        word.definition = request.POST.get('definition')

        show_word_user = request.POST.get('show_word_user')
        if (show_word_user == 'on'):
            word.show_user = True
        else:
            word.show_user = False
        word.save()
        return redirect('word_list_intranet')

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
        current_user = request.user
        category.register_author = current_user

        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')
        category.banner = request.FILES.get('image_uploads')

        show_category_user = request.POST.get('show_category_user')
        if (show_category_user == 'on'):
           category.show_user = True
        else:
            category.show_user = False


        category.save()
        return redirect('category_list_intranet')

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
    return redirect('category_list_intranet')


def category_list(request):
    categories = Word_Category.objects.filter(show_user=True)
    media_path = '/media/'
    context = {
        'media_path': media_path,
        'categories': categories,
        'title_page': 'Lista de Categorías',
        'is_active_category_list': 'active'
    }
    return render(request, 'dictionary/category/category_list.html', context)


def category_list_intranet(request):
    categories = Word_Category.objects.all().order_by('name')
    context = {
        'categories': categories,
        'title_page': 'Lista de Categorías',
        'is_active_category_list': 'active'
    }
    return render(request, 'dictionary/category/category_list_intranet.html', context)


def category_update(request, pk):
    users = User.objects.all()
    category = Word_Category.objects.get(pk=pk)
    categories = Word_Category.objects.all()
    if request.POST:
        current_user = request.user
        category.update_author = current_user

        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')

        if request.FILES.get('image_uploads'):
            category.banner = request.FILES.get('image_uploads')

        show_category_user = request.POST.get('show_category_user')
        if (show_category_user == 'on'):
            category.show_user = True
        else:
            category.show_user = False

        category.save()

        return redirect('category_list_intranet')
    context = {
        'category': category,
        'users': users,
        'categories': categories,
        'title_page': 'Actualización de Categoría'
    }

    return render(request, 'dictionary/category/category_update.html', context)
