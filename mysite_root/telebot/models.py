from django.db import models

# Create your models here.

class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Айди чата')
    tg_message = models.TextField(verbose_name='Текст сообщения')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.tg_chat

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"