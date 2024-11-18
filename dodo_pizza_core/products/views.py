from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pizza
from .seriailzers import PizzaSerializer, PizzaDetailSerializer


class PizzaListAPIView(APIView):
    """
    Вьюшка, чтобы вернуть список всех пицц.
    """
    def get(self, request, *args, **kwargs):
        pizza_list = Pizza.objects.all()
        serializer = PizzaSerializer(instance=pizza_list, many=True)
        response_body = serializer.data
        return Response(status=status.HTTP_200_OK, data=response_body)

class PizzaDetailAPIView(APIView):
    """
    Вьюшка, чтобы вернуть детальную информацию про пиццу.
    """
    def get(self, request, *args, **kwargs):
        try:
            pizza = Pizza.objects.get(id=kwargs['pk'])
        except Pizza.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Пицца не найдена'})

        serializer = PizzaDetailSerializer(instance=pizza, many=False)
        response_body = serializer.data
        return Response(status=status.HTTP_200_OK, data=response_body)
