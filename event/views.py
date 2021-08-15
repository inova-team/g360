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

    date_now = str(timezone.now())
    # timezone.activate("America/Lima")
    # Para conocer la ubicacion horaria de donde saca la hora
    # print(timezone.get_current_timezone())

    context = {
        'users': users,
        'title_page': 'Creacion de Eventos',
        'is_active_event_upload': 'active',
        'date_min': date_now[:10] + 'T' + date_now[11:16]
    }

    # print(date_now[:10] + 'T' + date_now[11:16])

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

    date_event = str(event.date_event)
    date_now = str(timezone.now())

    context = {
        'event': event,
        'users': users,
        'title_page': 'Actualizacion de Eventos',
        'is_active_event_upload': 'active',
        'date_min': date_now[:10] + 'T' + date_now[11:16],
        'date_event': str(date_event[:10] + 'T' + date_event[11:16])
    }

    # print(str(event.date_event))
    # print(context['date_event'])
    
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


def event_repository(request):
    events = Event.objects.all()
    date_now = str(timezone.now())
    #print(date_now[:10] + 'T' + date_now[11:19])
    context = {
        'events': events,
        'title_page': 'Eventos',
        'date_now': date_now[:10] + 'T' + date_now[11:16]
    }
    return render(request,'event/event_repository.html',context)


@login_required(login_url='g360Login')
def event_detail(request, pk):
    event = Event.objects.filter(pk=pk).exists()
    if event:
        event = Event.objects.get(pk=pk)
        list_events = Event.objects.order_by('-date_event').exclude(pk=pk)[0:3]
        context = {
            'event': event,
            'title_page': event.name,
            'list_events': list_events
        }
        return render(request, 'event/event_detail.html', context)
    return redirect('home')