from django import forms
from django.forms import ModelForm, fields
from .models import Gastos

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['nome', 'preco', 'tipo', 'data']
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': "form-control", 'label': 'Nome do Gastos'
                }),
            'preco': forms.NumberInput(
                attrs={
                    'class': "form-control", 'label':'Preço'
                }
            ),
            'data': forms.DateInput(
                attrs={
                    'class': "form-control", 'label':'Data de Gasto', 'type':'date',

                }
            ),
            'tipo': forms.Select(
                    attrs={
                        'class': "form-control",
                    }
                )
        }

'''class GastosForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Gasto',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
            }
        )
    )
    preco = forms.DecimalField(
        label='Preço',
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    tipo = forms.ChoiceField(
        choices=[
            ('',''),
            ('Mercado','Mercado'),
            ('Farmácia','Farmácia'),
            ('Casa', 'Casa'),
        ],
        widget=forms.Select(
            attrs={
                'class': "form-control",
            }
        )
    )
    data = forms.DateField(
        label='Data de Gastos realizados',
        widget=forms.DateInput(
            attrs={
                'class': "form-control",
            }
        )
    )'''