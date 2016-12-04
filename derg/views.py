# -*- coding:utf-8 -*-
import user

from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import *
from django.core.context_processors import csrf
from  django import *
from django.views.generic import FormView

from derg.forms import LoginForm,LogoutForm


def base(request):
    return render_to_response('derg/base.html')


# def login(request):
#     form = LoginForm()
#
#     # у тебя ошибка была в том что ты пост не там смотрел,
#     # request.method vs request.POST
#     # Если весь код вернуть обратно, и поменять снова на request.method, то вероятность что все заработает 95%
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print 3
#         errors = []
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 print 1
#                 return redirect("/")
#             else:
#                 print 2
#                 errors = "User not found"
#                 return redirect("/",errors)
#     return render(request, 'derg/base.html', {'form': form})
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect("/")


class LoginView(FormView):
    """Авторизация"""
    template_name = 'derg/base.html'
    form_class = AuthenticationForm
    success_url = '/'



    # def form_invalid(self, form):
    #     error = form.confirm_login_allowed
    #     return redirect('/',error)
    def form_valid(self, form):
        user = form.get_user()
        if user.is_active:
            auth.login(self.request, user)
            return redirect('/')



class LogoutView(RedirectView):
    """Выход"""
    # permanent = True

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')

