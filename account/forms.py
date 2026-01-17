from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()


class SignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-label','placeholder':'Must contain 8 characters'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-label','placeholder':'Confirm password'}))

    class Meta:
        model = user
        fields = ['username','phone','email','password']


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data[password]
        confirm_password = cleaned_data[confirm_password]

        if password != confirm_password:
            raise forms.ValidationError('Password is not correct')
        