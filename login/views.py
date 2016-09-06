# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if not request.user.is_anonymous():
        return redirect('main')
    context = {'title': 'Вход'}
    return render(request, 'login.html', context)
