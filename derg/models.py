# -*- coding:utf-8 -*-
from django.db import models

""" С большой буквы =) Article """
class article(models.Model):
    like = models.IntegerField(default=0)
    text = models.TextField()
    title = models.CharField(max_length=100)
