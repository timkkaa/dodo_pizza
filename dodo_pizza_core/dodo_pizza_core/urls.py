"""
URL configuration for dodo_pizza_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import PizzaListAPIView, PizzaDetailAPIView, DrinkDetailAPIView, DrinkListAPIView
from users.views import UserRegistrationAPIView, UserLoginApiView, SayHelloAPIView, PizzaCommentAPIView

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Бэкенд документация API для Додо сервера",
      default_version='v1',
      description="API предостовляет возможность заригистрировать, логинитсяб смотреть пиццы и коментировать их",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
    path('api/v1/pizzas/<int:pk>/', PizzaDetailAPIView.as_view(), name='pizza-detail'),
    path('api/v1/drinks/', DrinkListAPIView.as_view(), name='drink-list'),
    path('api/v1/drinks/<int:pk>/', DrinkDetailAPIView.as_view(), name='drink-detail'),
    path('api/v1/user/registration/', UserRegistrationAPIView.as_view(), name='user-registration-url'),
    path('api/v1/user/login/', UserLoginApiView.as_view(), name='user-login-url'),
    path('api/v1/user/login/', UserLoginApiView.as_view(), name='user-login-url'),
    path('api/v1/say-hello/', SayHelloAPIView.as_view()),
    path('api/v1/pizzas/<int:pk>/comment/', PizzaCommentAPIView.as_view()),
]
#{
#    "phone_number":"0771484819",
#    "password":"qwerty1234"
#0312312312
#timurk010909
#}