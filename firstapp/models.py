# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Firstapp(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.description)

