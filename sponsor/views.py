from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import User
from sponsor.models import Sponsor


def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
        'title_page': 'Lista de Sponsor',
        'is_active_article_list': 'active'
    }
    return render(request, 'sponsor/sponsor_list.html', context)

def sponsor_upload(request):
    users = User.objects.all()
    if request.POST:
        sponsor = Sponsor()
        if request.POST.get('author_select') != "0":
            author_select = User.objects.get(pk=request.POST.get('author_select'))
            sponsor.author = author_select

        sponsor.name = request.POST.get('name')
        sponsor.description = request.POST.get('description')
        sponsor.banner = request.FILES.get('image_uploads')
        sponsor.type = request.POST.get('type')

        if 'fb_link' in request.POST:
            sponsor.fb_link = request.POST.get('fb_link')

        if 'instagram_link' in request.POST:
            sponsor.instagram_link = request.POST.get('instagram_link')

        if 'twitter_link' in request.POST:
            sponsor.twitter_link = request.POST.get('twitter_link')

        if 'website_link' in request.POST:
            sponsor.website_link = request.POST.get('website_link')

        sponsor.save()
        return redirect('sponsor_list')

    context = {
        'users': users,
        'title_page': 'Creación de Sponsor',
        'is_active_sponsor_upload': 'active'
    }
    return render(request, 'sponsor/sponsor_upload.html', context)

def sponsor_delete(request, pk):
    sponsor = Sponsor.objects.get(pk=pk)
    sponsor.delete()
    return redirect('sponsor_list')