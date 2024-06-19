from django import forms
from .models import Maquinas

class formulariomaquina(forms.ModelForm):
    class Meta:
        model = Maquinas
        fields = ('nome', 'codigo', 'status')