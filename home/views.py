from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template


def renderHome(request):
    context = {
        'title_page' : 'Home',
    }
    return render(request, 'home/home.html', context)

def renderContactUs_email(request):
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
def renderIntranet(request):
    context = {
        'title_page': 'Intranet',
        'is_active_intranet': 'active'
    }
    return render(request, 'intranet/intranet.html', context)