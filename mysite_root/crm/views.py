from django.shortcuts import render
from . models import Order
from . forms import OrderForm

# Create your views here.

def first_page(request):
    # Получаем все эксземпляры класса Order (все строки из таблицы Заказы)
    object_list = Order.objects.all()
    # Cоздадим экземпляр формы
    form = OrderForm()
    # Отрисовываем полученные данные на странице index.html
    return render(request, './index.html', {
        'object_list': object_list,
        'form': form,
    })
def thanks_page(request):
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
    return render(request, './thanks_page.html', {
        'name': name,
        'phone': phone,
    })