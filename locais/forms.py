from django import forms
from .models import Locais

class FormularioLocais(forms.ModelForm):
    class Meta:
        model = Locais
        fields = ('usuario', 'local', 'maquina')