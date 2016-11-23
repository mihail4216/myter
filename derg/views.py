# -*- coding:utf-8 -*-
import user

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import *
from django.core.context_processors import csrf
from  django import *
from django.views.generic import FormView

from derg.forms import LoginForm,LogoutForm


def base(request):
    return render_to_response('derg/base.html')


def login(request):
    form = LoginForm()

    # у тебя ошибка была в том что ты пост не там смотрел,
    # request.method vs request.POST
    # Если весь код вернуть обратно, и поменять снова на request.method, то вероятность что все заработает 95%
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print 1
                return render_to_response("derg/base.html")
        else:
            args = {}
            args['login_error'] = "User is not found"
            return render_to_response("derg/base.html",args)
    return render(request, 'derg/base.html', {'form': form})


def logout(request):
    fo = LogoutForm(request.POST)
    auth.logout(request)
    return render_to_response("derg/base.html",{'form': fo})



