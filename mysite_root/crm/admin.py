from django.contrib import admin
from .models import StatusCrm, Order, CommentCrm

# Register your models here.
# Выведем комментарии непосредственно в карточке заказа
class Comment(admin.StackedInline):
    # Указываем обязательный атрибут - модель к которой относится данный класс
    model = CommentCrm
    # Указываем поля с которыми будем работать
    fields = ('comment_date', 'comment_text')
    readonly_fields = ('comment_date',)
    # Задаим одно поле ввода для модели Comment = 1, если указать 0 - необходимо нажимать зеленый плюс
    # для отображения поля комментария
    extra = 0

# Создадим класс для кастомизации админ панели приложения crm. Страница отбражения всех заказов
# Наслудуем от класса admin.ModelAdmin - класс для кастомизации админки
class OrderAdmin(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра заказов
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # Отмечаем поля по нажатию на которые можно перейти на траницу заказа
    list_display_links = ('id', 'order_name')
    # Добавляем поле поиска, передаем в него поля по которым будет осущ. поиск
    search_fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # Добавляем фильтр (запитая важна, если один элемент в кортеже)
    list_filter = ('order_status', )
    # Определяем поля, которые можно отредактировать, не переходя на отдельный заказ
    list_editable = ('order_status', 'order_phone',)
    # Разабьем вывод на несколко страниц.
    # Укажем сколько строк на одной странице
    list_per_page = 10
    # Укажем максимальное количество полей при выводе всех
    list_max_show_all = 100
    # Настроим карточку заказа
    fields = ('id', 'order_dt', 'order_status', 'order_name', 'order_phone')
    # Если не задать параметр readonly_fields? django выдаст ошибку, т.к. поле order_dt и id не изменяемые
    readonly_fields = ('id', 'order_dt')
    # Передадим класс Comment. По умолчанию одается 3 поля сторонней модели
    inlines = [Comment,]





# Зарегестрируем (добавим) в админ панели созданные нами модели
# admin.site.register(models.Order, OrderAdmin) - вторым классом добавлен класс кастомизации
admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

