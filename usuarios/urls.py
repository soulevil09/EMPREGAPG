from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name='home'),
    path('registro_candidato', registro_candidato, name='registro_candidato'),
    path('login_candidato', login_candidato, name='login_candidato'),
    path('completar_perfil', completar_perfil, name='completar_perfil'),
    path('logout_candidato', logout_candidato, name='logout_candidato'),
    path('registro_empregador', registro_empregador, name='registro_empregador'),
    path('login_empregador', login_empregador, name='login_empregador'),
    path('logout_empregador', logout_empregador, name='logout_empregador'),
    path('perfil_candidato', perfil_candidato, name='perfil_candidato'),
    path('perfil_empregador', perfil_empregador, name='perfil_empregador'),
    path('editar_candidato/', editar_candidato, name='editar_candidato'),
    path('editar_empregador/', editar_empregador, name='editar_empregador'),
]