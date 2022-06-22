from email import message
from multiprocessing import context
from os import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as signin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
    
    if request.user.is_authenticated:
        return redirect('main/')
    else:
    
        email = request.GET.get('email')
        password = request.GET.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            signin(request, user)
            return redirect('/')
        else:
            print('ni')
            messages.error(request, 'Адрес немесе парольды қате тердіңіз')
        
        context = {
            'message': message
        }
        
        return render(request, 'login.html', context)
    