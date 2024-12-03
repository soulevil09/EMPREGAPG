from django import forms
from .models import Vagas

class FormVagas(forms.ModelForm):
    class Meta:
        model = Vagas
        fields=('titulo','descricao')
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o título da vaga...'}),
            'descricao':forms.Textarea(attrs={'class':'form-control','placeholder':'Descrição da vaga...'})
        }