from django.db import models
from vagas.models import Vagas

class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    caracteristica_empresa = models.TextField()
    cnpj = models.CharField(max_length=14, unique=True, null=False)
    logo = models.ImageField(upload_to="logo_empresa", null=True)

    def __str__(self) -> str:
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa_id=self.id).count()

