# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Comment(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    date = models.DateTimeField()
    # user = models.ForeignKey(to='social.default.UserSocialAuth')
    parent = models.ForeignKey(to='self', blank=True, null=True)
