from django.db import models

# Create your models here.
# Создаем клас Order (название класса = название таблицы в БД), название полей, тип, параметры поля
class Order(models.Model):
    # order_dt - имя поля таблицы с типом DateTimeField
    order_dt = models.DateTimeField(auto_now=True)
    # verbose_name - имя поля отображаемого в админ панеле
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.order_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"