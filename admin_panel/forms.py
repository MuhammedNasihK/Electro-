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

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['brand'].empty_label = 'Select Brand...'
        self.fields['category'].empty_label = 'Select Category...'


class VariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['price','discount_price','stock']
        widgets = {
            'price': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'discount_price': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'stock': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
        }

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['spec', 'value']

        widgets = {   
            'spec': forms.Select(attrs={'class':'form-select form-select-sm'}), 
            'value': forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'e.g. 5000 mAh'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['spec'].empty_label = "Select Specification..."


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


SpecificationFormSet = inlineformset_factory(
    Product, 
    Specification, 
    form=SpecificationForm, 
    extra=23, 
    can_delete=True
)