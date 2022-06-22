from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Family, Needy, StatusHome, Category, StatusType, Event
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django_admin_geomap import geomap_context
import requests
import hashlib
from random import randint
from datetime import datetime
import xmltodict
def main(request):
    
    return render(request, 'landing-page.html', {})


@login_required(login_url='/auth/login')
def NeedyList(request):
        
    categories = Category.objects.all()
    status_types = StatusType.objects.all()
    needies = Needy.objects.all()
      
    context= {
        "categories": categories,
        "needies": needies,
        "status_types": status_types, 
    }
    return render(request, 'index.html', context)

@login_required(login_url='/auth/login')
def NeedyListDetail(request):
    
    needies = Needy.objects.all().order_by('status')
    
    context= {
        "needies": needies,  
    }
    return render(request, 'second.html', context)

@login_required(login_url='/auth/login')
def NeedyListDetailInfo(request, pk):
    
    geomap_items = geomap_context(Needy.objects.filter(id=pk))
  
    return render(request, 'needy_info.html', geomap_items)

@login_required(login_url='/auth/login')
def NeedyFamilyList(request):
    
    families = Family.objects.all()

    context= {
        "families": families,     
    }
    return render(request, 'needy_family.html', context)

@login_required(login_url='/auth/login')
def NeedyFamilyInfo(request, pk):
    
    return render(request, 'needy_family_info.html', geomap_context(Family.objects.filter(id=pk)))

@login_required(login_url='/auth/login')
def NeedyFamilyList(request):
    
    families = Family.objects.all()
  
    context= {
        "families": families,
    }
    return render(request, 'needy_family.html', context)

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

def payment(request): 
    url = 'init_payment.php'
    secret_key = '28pEVtditkTilolL'
    pg_merchant_id = 544317
    hash_object = ''
    pg_sig = ''
    redirect_url = ''
    
    
    def sort_list(var):
        data_value = ''
        sorted_tuple = sorted(var.items(), key=lambda x: x[0])
        for k in sorted_tuple:
            print(str(k[1]))
            data_value = data_value + str(k[1])+ ';'
        data_value = url + ';' + data_value + '' + secret_key
        hash_object = hashlib.md5(data_value.encode('utf-8')).hexdigest()
        return hash_object
    
    try:
        if request.POST:
            email = request.POST.get('email')
        number_phone = request.POST.get('number_phone')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        var = {
            
            'pg_amount':amount,
            'pg_description':'Тест',
            'pg_merchant_id':pg_merchant_id,
            'pg_order_id': randint(0, 10000),
            'pg_salt':'Тест',
            'pg_currency': 'KZT',
            'pg_success_url': 'https://google.com',
            'pg_failure_url': 'https://youtube.com',
            'pg_user_phone': 77089531792,
            'pg_payment_method': 'bankcard', 
            'pg_user_contact_email': email,
        }
        
        pg_sig = sort_list(var)
        var['pg_sig']= pg_sig
        print(name)
        
        r = requests.post('https://api.paybox.money/init_payment.php', data=var)
        
        return redirect(xmltodict.parse(r.text)['response']['pg_redirect_url']) 
    except Exception:
        print(number_phone)
        print('eror')
    
    
    return render(request, 'payment.html', {})
    
    
            
    

