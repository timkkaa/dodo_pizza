
from rest_framework import serializers
from .models import Pizza, Drink


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'image',
            'size'
        )

class PizzaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'image',
            'consist',
            'is_new',
            'size',
            'weight'
        )

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'price', 'volume', 'image')   # Для напитков

class DrinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'price', 'volume', 'image', 'is_cold')  # Для детальной информации