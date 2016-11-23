# -*- coding:utf-8 -*-
"""  вот эта строчка нужна для того чтобы пайчарм воспринимал русские символы, даже если ты не будешь тут писать, но
напишешь print user.name , а оно на русском, у тебя пайчарм сразу заорет об ошибке, типа не может прочитать """
from django.conf.urls import include, url
from derg.views import *


""" юрл лучше импортировать, потом легчк будет тебе самому найти функцию, ctrl + клик по названию, быстро перейдешь """
urlpatterns = [
    url(r'^$', login , name='login'),
    url(r'^logout/$',logout, name='logout'),
    # url(r'^$','derg.views.base' ,name="base"),
]
