from django.db import models

# Create your models here.

class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    # Измененеие отображения имени объекта. __str__ - это строковое представление объекта
    # Получим корректное отображение имени объекта в админ паненле
    def __str__(self):
        return self.cms_title

    # Изменение отображения имени класса, в единственном и множественном числе
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"