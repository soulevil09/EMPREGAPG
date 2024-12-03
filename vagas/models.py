from django.db import models

class Vagas(models.Model):
    empresa = models.ForeignKey('empresa.Empresa', null=True, on_delete=models.CASCADE)
    empregador = models.ForeignKey('usuarios.Empregador', null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
