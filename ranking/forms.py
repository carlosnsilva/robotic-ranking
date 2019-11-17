from django import forms
from .models import cadastro

class Insertcadastro(forms.ModelForm):

    class Meta:
        model = cadastro


        fields = [
            'nome',
            'campus',
            'tempo',
            'volta',
            'penalidade'
        ]