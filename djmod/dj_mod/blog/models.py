# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class post(models.models):
     activo = models.BooleanField(default=True)
     titulo = models.CharField(max_length=45,null=True)

     def __str__(self):
         return str(self.titulo)
