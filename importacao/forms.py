from django import forms
from .models import Arquivo

class FormularioDeArquivo(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ('arquivo',)
