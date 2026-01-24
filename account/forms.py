from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Must contain characters'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Must contain 4 characters'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

    class Meta:
        model = user
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError('Password must contain 4 characters')
        confirm_password = cleaned_data.get('confirm_password')
    
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password not matching')
        
        return cleaned_data
    

class LoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter registered email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))



class ForgotEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Registerd Email'}))