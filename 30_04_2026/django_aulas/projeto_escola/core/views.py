from django.shortcuts import render, get_object_or_404
from .models import Livro


def inicio(request):
    return render(request, 'core/inicio.html')


def sobre(request):
    return render(request, 'core/sobre.html')


def curso(request):
    contexto = {
        'nome_curso': 'Curso Tecnico em Desenvolvimento de Sistemas',
        'professor': 'Professor Exemplo',
        'carga_horaria': 1200,
        'disciplinas': ['Python', 'Banco de Dados', 'Django', 'HTML e CSS'],
        'turno': 'Noturno',
    }
    return render(request, 'core/curso.html', contexto)


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'core/lista_livros.html', {'livros': livros})


def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'core/detalhe_livro.html', {'livro': livro})
