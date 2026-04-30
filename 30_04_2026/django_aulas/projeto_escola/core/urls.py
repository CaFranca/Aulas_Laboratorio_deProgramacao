from django.urls import path
from .views import inicio, sobre, curso

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('curso/', curso, name='curso'),
]
