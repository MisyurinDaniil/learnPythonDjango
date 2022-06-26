from django.db import models

# Create your models here.

class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.status_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

# Создаем клас Order (название класса = название таблицы в БД), название полей, тип, параметры поля
class Order(models.Model):
    # order_dt - имя поля таблицы с типом DateTimeField
    order_dt = models.DateTimeField(auto_now=True)
    # verbose_name - имя поля отображаемого в админ панеле
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    # Связываем таблицы через тип поля ForeignKey, вторым параметром указывается что делать при
    # удалении поля (on_delete=models.PROTECT - запрещает удалять поля при удалении родителя)
    # blank - для пустоты в админ панели django
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.order_name

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

# Создаем класс комментарий
class CommentCrm(models.Model):
    # Связываем таблицы через тип поля ForeignKey
    # on_delete=models.CASCADE - при удалении родителя удаляться и все связанные с ним поля (комментарии к нему)
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='текст комментария')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.comment_text

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"