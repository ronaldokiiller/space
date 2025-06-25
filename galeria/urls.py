from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imagens, name='lista_imagens'),# incluido para ajustar o ReverseMatch
    path('imagem/', views.imagem, name='imagem'),
    path('nova/', views.criar_imagem, name='criar_imagem'),
    path('editar/<int:pk>/', views.editar_imagem, name='editar_imagem'),
    path('deletar/<int:pk>/', views.deletar_imagem, name='deletar_imagem'),

]