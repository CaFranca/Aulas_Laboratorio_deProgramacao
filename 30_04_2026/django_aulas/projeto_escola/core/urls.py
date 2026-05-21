from django.urls import path
from .views import inicio, sobre, curso, lista_livros, detalhe_livro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('curso/', curso, name='curso'),
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/<int:id>/', detalhe_livro, name='detalhe_livro'),
]
