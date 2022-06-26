from django.shortcuts import render
from . models import Order
from . forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram

# Create your views here.

def first_page(request):
    # Получаем данные
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(id=1)
    pc_2 = PriceCard.objects.get(id=2)
    pc_3 = PriceCard.objects.get(id=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    # Объеденим все переменные в один словарь
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form' : form,
    }
    # Отрисовываем полученные данные на странице index.html
    return render(request, './index.html', dict_obj)
def thanks_page(request):
    if request.POST:
        # Принемаем данные переданные формой методом Get
        # name = request.GET['name']
        # phone = request.GET['phone']
        # Принемаем данные переданные формой методом POST
        name = request.POST['name']
        phone = request.POST['phone']
        # Создаем экземпляр класса Order
        element = Order(order_name = name, order_phone = phone)
        # Записываем данные в таблицу
        element.save()
        sendTelegram(name, phone)
        return render(request, './thanks.html', {
            'name': name,
        })
    else:
        return render(request, './thanks.html')