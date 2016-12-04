# -*- coding:utf-8 -*-
"""  вот эта строчка нужна для того чтобы пайчарм воспринимал русские символы, даже если ты не будешь тут писать, но
напишешь print user.name , а оно на русском, у тебя пайчарм сразу заорет об ошибке, типа не может прочитать """
from django.conf.urls import include, url
from django.views.generic import TemplateView

from derg.views import *
from derg.views import LogoutView,LoginView

""" юрл лучше импортировать, потом легчк будет тебе самому найти функцию, ctrl + клик по названию, быстро перейдешь """
urlpatterns = [
    url(r'^$', LoginView.as_view(template_name='derg/base.html' ) , name='login'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
    url(r'^about/', TemplateView.as_view(template_name='derg/about.html'),name='about'),
    # url(r'^about/', AboutView.as_view(), name='about'),
    # url(r'^$','derg.views.base' ,name="base"),
]
