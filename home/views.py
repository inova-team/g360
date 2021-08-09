from django.shortcuts import render

# Create your views here.

def renderHome(request):
    context = {
        'title_page' : 'Home',
    }
    return render(request, 'home/home.html', context)