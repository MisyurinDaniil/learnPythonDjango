from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.pc_value

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Цены"
        verbose_name_plural = "Цена"

class PriceTable(models.Model):
    pc_title = models.CharField(max_length=20, verbose_name='Услуга')
    pc_old_price = models.CharField(max_length=20, verbose_name='Старая цена')
    pc_new_price = models.CharField(max_length=20, verbose_name='Новая цена')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.pc_title

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуга"
