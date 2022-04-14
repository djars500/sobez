from http.client import NOT_EXTENDED
import imp
from traceback import print_tb
from unicodedata import category
from django.shortcuts import render
from .models import Needy, StatusHome, Category, StatusType, Event
from authentication.models import User
from django.contrib.auth.decorators import login_required


def main(request):
    
    context = {
        
    }
    return render(request, 'landing-page.html', context)



@login_required(login_url='/auth/login')
def NeedyList(request):
    categories = Category.objects.all()
    status_types = StatusType.objects.all()
    needies = Needy.objects.all()
    user = User.objects.all()
    
    
    
    context= {
        "users": user,
        "categories": categories,
        "needies": needies,
        "status_types": status_types,
        
    }
    return render(request, 'index.html', context)

@login_required(login_url='/auth/login')
def NeedyListDetail(request):
    
    needies = Needy.objects.all().order_by('status')
    user = User.objects.all()
    
    
        
    
    
    context= {
        "users": user,
        "needies": needies,
        
        
    }
    return render(request, 'second.html', context)


@login_required(login_url='/auth/login')
def EvenList(request):
    
    typeStr = request.GET.get('type')
    
    
    if typeStr == None:
        events = Event.objects.all().order_by('created_at')
    else:
        events = Event.objects.filter(type=typeStr)
    
    cash_in_row = Event.objects.filter(type='Аударылды')
    cash_out_row = Event.objects.filter(type='Берілді')
    cash_in = 0
    cash_out = 0
    for money in cash_out_row:
        cash_out += money.cash

    for money in cash_in_row:
        cash_in += money.cash
        
    total = cash_in - cash_out
        
        
    context = {
        'total': total,
        'cash_in': cash_in,
        'cash_out': cash_out,
        'events': events
    }
    
    return render(request, 'event.html', context)
    
    
    
            
    

