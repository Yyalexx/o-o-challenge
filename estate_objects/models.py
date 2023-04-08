from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

from estate_objects.config import *


class EstateObject(models.Model):
    division = models.CharField(max_length=2, choices=DIVISIONS, verbose_name='Округ')
    district = models.CharField(max_length=32, choices=DISTRICTS, verbose_name='Район')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    obj_type = models.CharField(max_length=16, choices=OBJ_TYPES, verbose_name='Тип объекта')
    condition = models.CharField(max_length=32, choices=CONDITIONS, verbose_name='Состояние объекта')
    area = models.FloatField(validators=[MinValueValidator(0)], verbose_name='Площадь объекта')
    owner = models.CharField(max_length=256, verbose_name='Собственник')
    current_holder = models.CharField(max_length=256, verbose_name='Фактический пользователь')
    media_files = models.FileField(upload_to='photo_video/', verbose_name='Фото/видео')

    def __str__(self):
        return f'Объект №{self.pk}'

    def get_absolute_url(self):
        return reverse('object_details', kwargs={'pk': self.pk})


class AdditionalFieldsList(models.Model):
    field_name = models.CharField(max_length=64, verbose_name='Название поля')
    field_type = models.CharField(max_length=1, choices=FIELD_TYPES, verbose_name='Тип поля')


class AdditionalFields(models.Model):
    obj_id = models.ForeignKey(EstateObject, on_delete=models.CASCADE)
    field_id = models.ForeignKey(AdditionalFieldsList, on_delete=models.CASCADE)
    int_value = models.IntegerField(null=True)
    str_value = models.CharField(max_length=256, null=True)
    date_value = models.DateTimeField(null=True)
    binary_value = models.FileField(upload_to='additional_files/', null=True)
