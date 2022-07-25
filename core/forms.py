from logging import PlaceHolder
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField

#for captcha fields later
# https://tryolabs.com/blog/2012/03/02/django-adding-captcha-validation-forms

    
    


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password',
                               widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2  = forms.CharField(label = 'Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields = ('username','email')
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder':'username'}),
            
            'email' : forms.TextInput(attrs = {'placeholder':'email here','class':'email_field'})
        }
    
    def clean_password2(self):
        cd = self.cleaned_data  
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont\'t match.')
        return cd['password2']