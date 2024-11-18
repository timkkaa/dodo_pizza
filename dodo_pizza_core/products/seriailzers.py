
from rest_framework import serializers
from .models import Pizza

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