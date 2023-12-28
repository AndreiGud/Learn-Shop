from django.db import models
from django.urls import reverse


# Create your models here.


class type_every(models.Model):
    name = models.CharField(max_length=200, help_text="Выберите общий класс предмета",
                            verbose_name="Общий класс предмета")

    def __str__(self):
        return self.name


class types_item(models.Model):
    name = models.CharField(max_length=200, help_text="Выберите тип класса предмета",
                            verbose_name="Тип класса предмета")

    def __str__(self):
        return self.name


class item_catalog(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Заголовок предмета")
    desc = models.TextField(max_length=1000, help_text="краткое описание",
                            verbose_name="Описание предмета",
                                   blank=True)
    type_item = models.ManyToManyField(type_every, help_text="Выберите тип для сортировки по общему классу",
                                       verbose_name="Общий класс",
                                       blank=True)
    types_item = models.ForeignKey(types_item, on_delete=models.CASCADE, help_text="Выберите тип класса для сортировки",
                                   null=True,
                                   verbose_name="Тип класса предмета",
                                   blank=True)
    path_image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100,
                                   help_text="Изображение",
                                   verbose_name="Изображение",
                                   blank=True
                                   )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('booksn', args=[str(self.id)])
