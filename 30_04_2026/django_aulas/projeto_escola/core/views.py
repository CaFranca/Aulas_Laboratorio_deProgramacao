from django.shortcuts import render


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
