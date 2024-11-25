
from rest_framework import serializers

from users.models import CustomUser, UserPizzaComment
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
        fields = (
            'id',
            'name',
            'price',
            'volume',
            'image'
        )   # Для напитков

class DrinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = (
            'id',
            'name',
            'price',
            'volume',
            'image',
            'is_cold'
        )  # Для детальной информации

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            )

class UserPizzaCommentSerializer(serializers.ModelSerializer):
    author_user = CustomUserSerializer(many=False, source='user')
    class Meta:
        model = UserPizzaComment
        fields = (
            'id',
            'comment_text',
            'created_at',
            'author_user',
        )