from logging import PlaceHolder
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment
# from captcha.fields import CaptchaField

#for captcha fields later
# https://tryolabs.com/blog/2012/03/02/django-adding-captcha-validation-forms

    
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400'}
    )


class UserRegistrationForm(forms.ModelForm):

  
    username = forms.CharField(label = 'Username',
                               widget=forms.TextInput(attrs={'placeholder':'Username' ,'class' : "w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400"}))
    email  = forms.CharField(label = 'Email',widget=forms.EmailInput(attrs={'class': "w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400"}))
    password = forms.CharField(label = 'Password',
                               widget=forms.PasswordInput(attrs={'placeholder':'password' ,'class' : "w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400"}))
    password2  = forms.CharField(label = 'Repeat Password',widget=forms.PasswordInput(attrs={'class': "w-full px-3 py-2 border rounded-md dark:border-gray-700 dark:bg-gray-900 dark:text-gray-100 focus:dark:border-violet-400"}))

    class Meta:
        model  = User
        fields = ('username','email')
    
    
    def clean_password2(self):
        cd = self.cleaned_data  
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont\'t match.')
        return cd['password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)