from django import forms
from .models import *
from django.forms import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','brand','name','slug']
        widgets = {
            'category': forms.Select(attrs={'class':'form-select form-select-sm'}),
            'brand': forms.Select(attrs={'class':'form-select form-select-sm'}),
            'name': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'slug': forms.TextInput(attrs={'class':'form-control form-control-sm'})
        }

class VariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        # Notice: We removed 'attribute' from here! We will handle it dynamically in HTML
        fields = ['colour','price','discount_price','stock']
        widgets = {
            'colour': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'price': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'discount_price': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'stock': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
        }

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['spec','value']
        widgets = {
            'spec': forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder': 'e.g., Processor'}),
            'value': forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder': 'e.g., Snapdragon 8 Gen 2'})
        }

SpecificationFormSet = inlineformset_factory(
    Product, 
    Specification, 
    form=SpecificationForm, 
    extra=5, 
    can_delete=True
)