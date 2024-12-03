from django import forms
from empresa.models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model=Empresa
        fields=('nome','email','endereco','caracteristica_empresa','logo', 'cnpj')
        widgets={
            'nome':forms.TextInput(attrs={'class':'form-control','placeholder':'Digite seu nome...','name':'nome'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'email@email.com','name':'email'}),
            'endereco':forms.TextInput(attrs={'class':'form-control','placeholder':'Rua...','name':'endereco'}),
            'cnpj':forms.TextInput(attrs={'class':'form-control','placeholder':'CNPJ','name':'cnpj'}),
            'caracteristica_empresa':forms.Textarea(attrs={'class':'form-control','placeholder':'Caracteristicas da empresa','name':'caracteristica_empresa'}),
        }
