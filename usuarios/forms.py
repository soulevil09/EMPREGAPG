from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Candidato, Empregador

class CandidatoForms(forms.ModelForm):
    telefone = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control telefone-mask', 'placeholder': '(XX) XXXX-XXXX'})
    )

    class Meta:
        model = Candidato
        fields = ('nome', 'email', 'telefone', 'cpf', 'senha')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu Email'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf-mask', 'placeholder': 'Digite seu CPF'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        }

class PerfilCandidatoForms(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ('imagem', 'curriculo', 'area_atuacao', 'descricao')
        widgets = {
            'area_atuacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva sua área de atuação:'}),
            'descricao':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva um pouco mais sobre você:'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'curriculo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        }

class EditarCandidatoForms(forms.ModelForm):
    telefone = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXX-XXXX'})
    )
    class Meta:
        model = Candidato
        fields = ('nome', 'email', 'telefone', 'cpf', 'senha', 'imagem', 'curriculo', 'area_atuacao', 'descricao')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu Email'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf-mask', 'placeholder': 'Digite seu CPF'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
            'area_atuacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva sua área de atuação:'}),
            'descricao':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva um pouco mais sobre você:'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'curriculo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        }

class EmpregadorForms(forms.ModelForm):
    telefone = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control telefone-mask', 'placeholder': '(XX) XXXXX-XXXX'})
    )

    class Meta:
        model = Empregador
        fields = ('nome', 'email', 'telefone', 'cpf', 'senha','imagem')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu Email'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf-mask', 'placeholder': 'Digite seu CPF'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

class EditarEmpregadorForms(forms.ModelForm):
    telefone = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'})
    )

    class Meta:
        model = Empregador
        fields = ('nome', 'email', 'telefone', 'cpf', 'senha','imagem')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu Email'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf-mask', 'placeholder': 'Digite seu CPF'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }


