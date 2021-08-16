from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.utils import timezone

from event.models import Event
from sponsor.models import Sponsor


def render_home(request):
    media_path = '/media/'
    sponsors = Sponsor.objects.all()
    date_now = str(timezone.now())
    date_filter = date_now[:19]
    events = Event.objects.filter(date_event__lt=date_filter).order_by('-date_event')[0:3]
    context = {
        'sponsor_active_pk': sponsors[0].pk,
        'sponsors': sponsors,
        'title_page': 'Home',
        'media_path': media_path,
        'is_active_home': 'active',
        'events': events
    }
    return render(request, 'home/home.html', context)


def render_contact_us_email(request):
    data = {}
    if request.POST:

        try:
            name = request.POST['name']
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')

            subject = f'Mensaje de {name}'
            sender = 'alonso.jake2000@gmail.com'
            recipients = ['alonso.jake2000@gmail.com']  # [email]
            # send_mail(subject, message, sender, recipients, fail_silently=True)

            context = {
                'name': name,
                'email': email,
                'number': number,
                'message': message,
            }

            template = get_template('assets/body_email.html')
            content = template.render(context)
            email = EmailMultiAlternatives(subject, '', sender, recipients, cc=[email])
            email.attach_alternative(content, 'text/html')
            email.send()

            data['exito'] = 'Se envió el correo con éxito'

        except Exception as e:

            data['error'] = str(e)

        return JsonResponse(data)


#@login_required(login_url='')
def render_intranet(request):
    context = {
        'title_page': 'Intranet',
        'is_active_intranet': 'active'
    }
    return render(request, 'intranet/intranet.html', context)