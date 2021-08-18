from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from article.models import Article
from event.models import Event
from slider_home.models import SliderItem


def slider_upload(request):
    events = Event.objects.all()
    articles = Article.objects.all()
    choices_items = ['Evento', 'Articulo']

    if request.POST:
        item = SliderItem()

        data_from_html = request.POST
        # print("===========")
        # print(data_from_html)

        type = {
            'Evento' : 'Event',
            'Articulo': 'Article'
        }

        item_type = data_from_html['item_type']
        print(data_from_html)

        if item_type == 'Evento':
            item.event = Event.objects.get(pk=data_from_html['item_selected'])

        elif item_type == 'Articulo':
            item.article = Article.objects.get(pk=data_from_html['item_selected'])

        item.type_item = type[item_type]
        item.save()

        return redirect('slider_list')

    context = {
        'events': events,
        'articles': articles,
        'title_page': 'Añadir item al Slider',
        'choices_items': choices_items,
        'is_active_slider_upload': 'active'
    }

    return render(request,'slider_home/slider_upload.html', context)


@login_required(login_url='g360Login')
def slider_delete(request, pk):
    item = SliderItem.objects.get(pk=pk)
    item.delete()
    return redirect('slider_list')


def slider_update(request):
    return render(request, 'home/home.html')


@login_required(login_url='g360Login')
def slider_list(request):
    items = SliderItem.objects.all()

    context = {
        'items': items,
        'title_page': 'Listado de Items del Slider',
        'is_active_slider_list': 'active'
    }

    return render(request, 'slider_home/slider_list.html', context)



def list_items_options(request):
    type_item = request.POST['type_item']
    #print("================")
    #print(type_item)

    # type = {
    #     'Evento': 'Event',
    #     'Articulo': 'Article'
    # }
    ser_instace = None

    #items = type[str(type_item)].objects.all()
    #print(items)
    #print(type[str(type_item)])

    if type_item == 'Evento':
        items = Event.objects.all()
        ser_instace = serializers.serialize('json', items)

    elif type_item == 'Articulo':
        items = Article.objects.all()
        ser_instace = serializers.serialize('json', items)

    # print(ser_instace)

    return JsonResponse({'item': ser_instace}, status=200)
