# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Comment(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    date = models.DateTimeField()
    user = models.ForeignKey(to='User')
    parent = models.ForeignKey(to='self', blank=True, null=True)


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
