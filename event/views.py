from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from authentication.models import Staff
from event.models import Event
from django.utils import timezone


@login_required(login_url='g360Login')
def event_upload(request):
    users = Staff.objects.all()

    if request.POST:
        event = Event()

        data_from_html = request.POST

        event.name = data_from_html['name']
        event.description = data_from_html['description']

        if data_from_html['responsible_select'] != 0:
            event.responsible = Staff.objects.get(id=data_from_html['responsible_select'])

        event.date_event = data_from_html['date_event']
        event.link_event = data_from_html['url_event']
        event.link_form = data_from_html['url_form']
        id_current_user = request.user.pk
        event.user_register = Staff.objects.get(user_id=str(id_current_user))
        event.user_last_update = Staff.objects.get(user_id=str(id_current_user))
        event.banner = request.FILES.get('image_uploads')
        event.save()
        return redirect('event_list')

    context = {
        'users': users,
        'title_page': 'Creacion de Eventos',
        'is_active_event_upload': 'active',
        'date_min': str(timezone.now())[:10]
    }

    return render(request, 'event/event_upload.html', context)


@login_required(login_url='g360Login')
def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return redirect('event_list')


@login_required(login_url='g360Login')
def event_update(request, pk):
    users = Staff.objects.all()
    event = Event.objects.get(pk=pk)

    if request.POST:

        data_from_html = request.POST

        event.name = data_from_html['name']
        event.description = data_from_html['description']

        if data_from_html['responsible_select'] != 0:
            event.responsible = Staff.objects.get(id=data_from_html['responsible_select'])

        event.link_event = data_from_html['url_event']
        event.link_form = data_from_html['url_form']
        id_current_user = request.user.pk
        event.user_last_update = Staff.objects.get(user_id=str(id_current_user))

        if request.FILES.get('image_uploads'):
            event.banner.delete()
            event.banner = request.FILES.get('image_uploads')

        event.save()
        return redirect('event_list')

    context = {
        'event': event,
        'users': users,
        'title_page': 'Actualizacion de Eventos',
        'is_active_event_upload': 'active',
        'date_min': str(timezone.now())[:10],
        'date_event': str(event.date_event)
    }

    #print(event.date_event)

    return render(request, 'event/event_update.html', context)


@login_required(login_url='g360Login')
def event_list(request):
    events = Event.objects.all()

    context = {
        'events': events,
        'title_page': 'Lista de Eventos',
        'is_active_event_list': 'active'
    }

    return render(request, 'event/event_list.html', context)


@login_required(login_url='g360Login')
def event_detail(request, pk):
    context = {
    }
    return render(request, 'event/event_detail.html', context)
