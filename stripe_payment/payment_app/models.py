from django.db import models


class Item(models.Model):
    """Модель товара"""
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price / 100
