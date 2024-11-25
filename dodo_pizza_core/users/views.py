from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser


class UserRegistrationAPIView(APIView):
    """Для регистрации"""

    def post(self, request, *args, **kwargs):
        request_body = request.data
        print('Тело запроса:', request_body)

        try:
            new_user = CustomUser.objects.create_user(
                phone_number=request_body['phone_number'],
                first_name=request_body['first_name'],
                last_name=request_body['last_name'],
                password=request_body['password']
            )
        except IntegrityError:
            return Response(status=400, data={
                'message': 'Такой пользователь уже существует'
            })

        token, created = Token.objects.get_or_create(user=new_user)

        return Response(
            status=201,
            data={
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'phone_number': new_user.phone_number,
                'token': token.key
            }
        )

class UserLoginApiView(APIView):

    def post(self, request, *args, **kwargs):
        request_body = request.data

        try:
            user = CustomUser.objects.get(phone_number=request_body['phone_number'])
            correct = user.check_password(request_body['password'])

            if not correct:
                return Response(status=400, data={'message': 'Вы ввели неверный пароль'})

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        except CustomUser.DoesNotExist:
            return Response(status=400, data={'message': 'Пользователь с таким номером не существует'})
        except KeyError:
            return Response(status=400,
                            data={'message': 'Пожалуйста, укажите номер телефона и пароль.'})

class SayHelloAPIView(APIView):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        return Response(status=200, data={'massage': f'Приве {current_user.first_name}'})

