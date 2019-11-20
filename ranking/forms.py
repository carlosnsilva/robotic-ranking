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
            'penalidade_1',
            'Valor_da_penalidade_1',
            'penalidade_2',
            'Valor_da_penalidade_2',
            'penalidade_3',
            'Valor_da_penalidade_3',
            'penalidade_4',
            'Valor_da_penalidade_4',
            'penalidade_5',
            'Valor_da_penalidade_5',
            'penalidade_6',
            'Valor_da_penalidade_6',
            'penalidade_7',
            'Valor_da_penalidade_7',
            'penalidade_8',
            'Valor_da_penalidade_8',
            'penalidade_9',
            'Valor_da_penalidade_9',
            'penalidade_10',
            'Valor_da_penalidade_10',
            'penalidade_11',
            'Valor_da_penalidade_11',
        ]