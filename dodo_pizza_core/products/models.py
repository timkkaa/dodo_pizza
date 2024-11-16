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
