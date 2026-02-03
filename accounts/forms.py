from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Must contain characters'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Must contain 4 characters'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError('Username must contain four characters')
        elif username.isdigit():
            raise forms.ValidationError("Username must contain Characters")
        password = cleaned_data.get('password')
        
        if len(password) < 4:
            raise forms.ValidationError('Password must contain four values')
        
        confirm_password = cleaned_data.get('confirm_password')
    
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password not matching')
        
        return cleaned_data
    

class LoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter registered email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))


class ForgotEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Registerd Email'}))


class ForgotOtpForm(forms.Form):
    otp1 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))
    otp2 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))
    otp3 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))
    otp4 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))
    otp5 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))
    otp6 = forms.CharField(max_length=1,widget=forms.TextInput(attrs={'class':'form-control otp-input'}))

    def get_otp(self):
        return (self.cleaned_data['otp1']+
                self.cleaned_data['otp2']+
                self.cleaned_data['otp3']+
                self.cleaned_data['otp4']+
                self.cleaned_data['otp5']+
                self.cleaned_data['otp6'])
    
class NewPasswordForm(forms.Form):
    password = forms.CharField(min_length=4,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter new password'}))
    confirm_password = forms.CharField(min_length=4,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter new password'}))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')

        if len(p1) < 4:
            raise forms.ValidationError('Password must contain four values')

        elif p1 and p2 and p1 != p2:
            raise forms.ValidationError('Password not matching')
        
        return cleaned_data