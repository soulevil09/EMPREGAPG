from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import format_number, PhoneNumberFormat
from django.core.exceptions import ValidationError
from phonenumbers.phonenumberutil import NumberParseException
from django.contrib.auth.hashers import make_password, check_password
from empresa.models import Empresa

class Candidato(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    telefone = PhoneNumberField(unique=True)
    cpf = models.CharField(max_length=14, primary_key=True)
    senha = models.CharField(max_length=128)

    imagem = models.ImageField(upload_to='imagens_perfil_candidato/', blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    area_atuacao = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.senha = make_password(self.senha)
        else:
            try:
                usuario_antigo = Candidato.objects.get(pk=self.pk)
                if usuario_antigo.senha != self.senha:
                    self.senha = make_password(self.senha)
            except Candidato.DoesNotExist:
                self.senha = make_password(self.senha)

        super(Candidato, self).save(*args, **kwargs)

    def clean(self):
        try:
            self.telefone = format_number(self.telefone, PhoneNumberFormat.E164)
        except NumberParseException:
            raise ValidationError('Número de telefone inválido')

    def check_password(self, senha_clara):
        return check_password(senha_clara, self.senha)

    def __str__(self):
        return self.nome

    
class Empregador(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    telefone = PhoneNumberField(unique=True)
    cpf = models.CharField(max_length=14, primary_key=True)
    senha = models.CharField(max_length=128)
    imagem = models.ImageField(upload_to='imagens_perfil_empregador/', blank=True, null=True)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.pk or not self.senha.startswith('pbkdf2_sha256$'):
            self.senha = make_password(self.senha)
        super(Empregador, self).save(*args, **kwargs)
    
    def clean(self):
        try:
            self.telefone = format_number(self.telefone, PhoneNumberFormat.E164)
        except NumberParseException:
            raise ValidationError('Número de telefone inválido')

    def check_password(self, senha_clara):
        return check_password(senha_clara, self.senha)

    def __str__(self):
        return self.nome
    




