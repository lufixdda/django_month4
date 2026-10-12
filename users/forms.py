from typing import Required

from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

GENDER = (
        ('М','М'),
        ('Ж','Ж')
    )

class LoginForm(AuthenticationForm):
       captcha = CaptchaField()


class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.CharField(required=True, initial='@gmail.com')
    phone_number = forms.CharField(max_length=15, required=True , initial='+996')
    gender = forms.ChoiceField(required=True, choices=GENDER)
    birthday = forms.DateField(required=True)
    relationship = forms.BooleanField(required=False, initial=False, label='В отношениях')
    url_blog = forms.URLField(label='есть ссылка на ютуб?', required=False)
    description = forms.CharField(max_length=400, required=False)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'photo',
            'password1',
            'password2',
            'email',
            'first_name',
            'phone_number',
            'gender',
            'birthday',
            'url_blog',
            'relationship',
            'description'
        )

        
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user