from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from alliance.models import Alliance

def alliance_list_user(request):
    media_path = '/media/'
    alliances = Alliance.objects.all()
    context = {
        'alliances': alliances,
        'media_path':media_path,
        'title_page': 'Alianzas',
        'is_active_alliances': 'active'
    }
    return render(request, 'alliance/alliance_list_user.html', context)



def alliance_list(request):
    alliances = Alliance.objects.all()
    context = {
        'alliances': alliances,
        'title_page': 'Lista de aliados',
        'is_active_alliance_list': 'active'
    }
    return render(request, 'alliance/alliance_list.html', context)

def alliance_upload(request):
    users = User.objects.all()
    if request.POST:
        alliance = Alliance()
        if request.POST.get('author_select') != "0":
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            alliance.author = author_select

        alliance.name = request.POST.get('name')
        alliance.description = request.POST.get('description')
        alliance.banner = request.FILES.get('image_uploads')
        alliance.type = request.POST.get('type')

        if 'fb_link' in request.POST:
            alliance.fb_link = request.POST.get('fb_link')

        if 'instagram_link' in request.POST:
            alliance.instagram_link = request.POST.get('instagram_link')

        if 'twitter_link' in request.POST:
            alliance.twitter_link = request.POST.get('twitter_link')

        if 'website_link' in request.POST:
            alliance.website_link = request.POST.get('website_link')

        alliance.save()
        return redirect('alliance_list')

    context = {
        'users': users,
        'title_page': 'Creación de aliado',
        'is_active_alliance_upload': 'active'
    }
    return render(request, 'alliance/alliance_upload.html', context)

def alliance_update(request, pk):
    users = User.objects.all()
    alliance = Alliance.objects.get(pk=pk)
    if request.POST:
        if request.POST.get('author_select') != "0":
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            alliance.author = author_select

        alliance.name = request.POST.get('name')
        alliance.description = request.POST.get('description')
        alliance.type = request.POST.get('type')

        alliance.fb_link = request.POST.get('fb_link')
        alliance.instagram_link = request.POST.get('instagram_link')
        alliance.twitter_link = request.POST.get('twitter_link')
        alliance.website_link = request.POST.get('website_link')

        if request.FILES.get('image_uploads'):
            alliance.banner = request.FILES.get('image_uploads')
        alliance.save()

        return redirect('alliance_list')
    context = {
        'alliance': alliance,
        'users': users,
        'title_page': 'Actualización de aliado'
    }
    return render(request, 'alliance/alliance_update.html', context)

def alliance_delete(request, pk):
    alliance = Alliance.objects.get(pk=pk)
    alliance.delete()
    return redirect('alliance_list')