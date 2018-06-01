# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Income, Expense, Token
from datetime import datetime
from django.shortcuts import render

# Create your views here.


@csrf_exempt
def submit_expense(request):
    """user submits an expense"""

#   TODO; validate data, user might be fake, token might be fake, amount might be...
    if 'date' not in request.POST:
        now = datetime.now()
    this_token = request.POST['token']
    print (this_token)
    this_user = User.objects.filter(token__token=this_token).get()
    print ("hello2")
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=now)
    #print ("i'm in submit expense")
    #print (request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """user submits an income"""

#   TODO; validate data, user might be fake, token might be fake, amount might be...
    if 'date' not in request.POST:
        now = datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=now)
    #print ("i'm in submit income")
    print (request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
