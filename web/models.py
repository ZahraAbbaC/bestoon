# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return "{}_token".format(self.user)


class Expense(models.Model):
    text = models.CharField (max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.date, self.amount)
 

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) #yani harkodum az in income ha b y user vasl mishan

    def __str__(self):
        return "{} - {}".format(self.date, self.amount)

