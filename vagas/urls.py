from django.urls import path
from .views import *

urlpatterns = [
    path('nova_vaga/', nova_vaga , name='nova_vaga'),
    path('vagas_candidato',vagas_candidato, name='vagas_candidato'),
    path('vagas_empregador', vagas_empregador, name='vagas_empregador'),
    path('vagas/<int:id>', vaga_unica, name='vaga_unica'),
    path('editar_vaga/<int:id>', editar_vaga, name='editar_vaga'),
    path('excluir_vaga/<int:id>', excluir_vaga, name='excluir_vaga'),
    path('<int:vaga_id>/candidatar/', candidatar_vaga, name='candidatar_vaga'),
    path('carregando_candidatura/', carregando_candidatura, name='carregando_candidatura')
]
