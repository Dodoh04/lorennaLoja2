from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('estoque/', views.estoque, name='estoque'),
    path('carros/', views.estoque, name='lista-carros'),
    path('carros/<int:pk>/', views.detalhe_carro, name='detalhe-carro'),
    path('leads/', views.criar_lead, name='criar-lead'),
    path('vendas/', views.lista_vendas, name='lista-vendas'),
    path('sobre-nos/', views.sobre_nos, name='sobre-nos'),
]