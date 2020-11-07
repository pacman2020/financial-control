from django import forms
from django.forms import fields
from .models import Product

class Productform(forms.ModelForm):
    name_product = forms.CharField(label='nome da produto', max_length=100, required=True)
    supplier_name = forms.CharField(label='nome do fornecedo', max_length=100, required=True)
    resale_value = forms.DecimalField(label='preço de revenda', required=True)
    commercial_value = forms.DecimalField(label='preço de comecial', required=True)
    amount = forms.IntegerField(label='quantidade', required=False)
    active = forms.BooleanField(label='tarefa ativa', required=False)

    class Meta:
        model = Product
        fields = (
            'name_product','supplier_name','resale_value',
            'commercial_value','amount','active',)