from django.urls import path
from .views import (
    inicio, sobre, curso,
    lista_livros, detalhe_livro,
    criar_livro, editar_livro, excluir_livro,
    signup
)
urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('curso/', curso, name='curso'),
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/<int:id>/', detalhe_livro, name='detalhe_livro'),
    path('livros/novo/', criar_livro, name='criar_livro'),
    path('livros/editar/<int:id>/', editar_livro, name='editar_livro'),
    path('livros/excluir/<int:id>/', excluir_livro, name='excluir_livro'),
    path('signup/', signup, name='signup'),
]