from django import forms
from .models import Item, Factory

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['factory'].queryset = Factory.objects.filter(name='公版')
        self.fields['factory'].label = '客戶名稱'
        self.fields['current_stock'].label = '當前庫存'
        self.fields['material'].label = '紙質'
        self.fields['product'].label = '品項'

    class Meta:
        model = Item
        fields = ['factory', 'product', 'material', 'current_stock']

class ItemForm_private(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['factory'].queryset = Factory.objects.exclude(name='公版')
        self.fields['factory'].label = '客戶名稱'
        self.fields['current_stock'].label = '當前庫存'
        self.fields['material'].label = '紙質'
        self.fields['product'].label = '品項'

    class Meta:
        model = Item
        fields = ['factory', 'product', 'material', 'current_stock']
