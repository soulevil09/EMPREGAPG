from django.urls import path
from . import views

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name='nova_empresa'),
    path('empresas/', views.empresas, name='empresas'),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name='excluir_empresa'),
    path('empresas/<int:id>', views.empresa, name='empresa_unica'),
    path('editar_empresa/<int:id>', views.editar_empresa, name='editar_empresa'),
    path('vincular_empresa', views.vincular_empresa, name='vincular_empresa'),
    # path('buscar-empresas/', views.buscar_empresas, name='buscar_empresas'),
    path('search/', views.search_empresas, name='search_empresas'),
    path('consulta_cnpj/', views.consulta_cnpj_ajax, name='consulta_cnpj'),

    # path('nova_vaga', views.nova_vaga, name='nova_vaga')
]
