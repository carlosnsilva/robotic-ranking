from django.urls import path
from .views import create, read, update, delete, pontuacao

urlpatterns = [
    path('', read, name = 'read'),
    path('cadastro', create, name = 'create'),
    path('rank.html', read, name = 'read'),
    path('update/<int:id>',update, name = 'update'),
    path('exluir/<int:id>', delete, name ='delete'),
    path('pontuacao/<int:id>', pontuacao, name ='pontuacao'),
]