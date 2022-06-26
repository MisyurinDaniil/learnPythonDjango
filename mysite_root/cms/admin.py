from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CmsSlider

# Register your models here.

class CmsAdmin(admin.ModelAdmin):
    # Кортеж с именами полей, который хотим отобразит в админ панеле на этапе просмотра слайдов
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    # Отмечаем поля по нажатию на которые можно перейти на страницу слайда
    list_display_links = ('cms_title',)
    # Определяем поля, которые можно отредактировать, не переходя на отдельный слайд
    list_editable = ('cms_css', )
    # Указжем поля отображаемые на карточке слайда
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    # Укажем поля только для чтения, чтобы django не вывалилвался в ошибку
    readonly_fields = ('get_img', )

    # Функция для отображения миниатюры картинки в админ панеле
    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'нет картинки'
    # Строковое представление функции get_img
    get_img.short_description = 'Миниатюра'

admin.site.register(CmsSlider, CmsAdmin)
