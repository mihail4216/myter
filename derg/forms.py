# -*- coding:utf-8 -*-
from django import forms


# class username(forms.Form):
#     usernames = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    """ Лучше пользоваться формой и объявлять ее тут, тут можно менять сам тип поля, тест, число, визивик повесить на поле
    В самом html этого не сможем сделать, но там можно как вначале ты делал так объявлять, для простых форм
    """
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())
class LogoutForm(forms.Form):
    logout = forms.BooleanField
