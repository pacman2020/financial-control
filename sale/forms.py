# from product.models import Product
# from django import forms
# from .models import Sale

# class FormSale(forms.ModelForm):
#     list_product = Product.objects.filter(active=True)

#     product_id = forms.ModelChoiceField(
#         queryset=list_product,
#         label='produto',
#         required=True
#         )
#     # um usuario pode compra mais de um produto

#     #preco total da compra e adicionado automaticamente pela quantidade
#     # purchase_price = forms.DecimalField(label='preço da compra', required=True)

#     amount = forms.IntegerField(label='quantidade', required=True)
#     active = forms.BooleanField(label='tarefa ativa', required=False)


#     model = Sale
#     fields = ('product_id','purchase_price','amount',
#             'active','create_at',)