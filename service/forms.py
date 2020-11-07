from django import forms
from .models import Service

class Serviceform(forms.ModelForm):
    name = forms.CharField(label='nome da servico', max_length=100, required=True)
    price = forms.DecimalField(label='preço da servico', required=True)
    active = forms.BooleanField(label='servico ativa', required=False)
    class Meta:
        model = Service
        fields = ('name','price','active',)