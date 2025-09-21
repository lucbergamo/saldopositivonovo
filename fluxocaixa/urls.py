from django.urls import path
from .views import index, gastos

urlpatterns = [
    path('', index, name='index'),
    path('gastos/', gastos, name='gastos'),
]