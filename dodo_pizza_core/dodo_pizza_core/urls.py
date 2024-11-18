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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
    path('api/v1/pizzas/<int:pk>/', PizzaDetailAPIView.as_view(), name='pizza-detail'),
    path('api/v1/drinks/', DrinkListAPIView.as_view(), name='drink-list'),
    path('api/v1/drinks/<int:pk>/', DrinkDetailAPIView.as_view(), name='drink-detail'),
]
