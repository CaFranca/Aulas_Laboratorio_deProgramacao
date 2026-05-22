from django.contrib import admin

from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'idade', 'ativo')
    search_fields = ('nome', 'matricula', 'curso')
    list_filter = ('ativo', 'curso')
