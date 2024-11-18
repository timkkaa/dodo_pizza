from django.db import models

from django.db import models

class Pizza(models.Model):
    """
    Модель для пицц
    """
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(help_text="Указывайте цену в сомах")
    image = models.ImageField(upload_to="pizza_images/")
    consist = models.TextField(verbose_name="Состав")
    is_new = models.BooleanField()
    size = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField(verbose_name="Вес в граммах")

    class Meta:
        verbose_name_plural = "Пиццы"
        verbose_name = "Пицца"

class Drink(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название напитка")
    price = models.PositiveIntegerField(help_text="Указывайте цену в сомах")
    volume = models.PositiveSmallIntegerField(verbose_name="Объем в л")
    image = models.ImageField(upload_to='drink_images/', verbose_name="Изображение")
    is_cold = models.BooleanField(default=True, verbose_name="Охлажденный")

    class Meta:
        verbose_name_plural = "Напитки"
        verbose_name = "Напиток"
