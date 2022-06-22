import hashlib
from django.shortcuts import render
from .models import Family, Needy, StatusHome, Category, StatusType, Event
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django_admin_geomap import geomap_context
import requests
import hashlib

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
    
    print('request')
    print(request.GET)
    
    # pg_merchant_id = 544317
    # secret_key = '28pEVtditkTilolL'
    
    # url = 'init_payment.php'
    # pg_amount = 25
    # pg_description = 'test'
    # pg_order_id = 23
    # pg_salt = 'ok'
    
    # var = {
    #     pg_order_id: '',
    #     pg_payment_id: 12,
    #     pg_amount: 12,
    #     pg_net_amount: 1,
    #     pg_currency: 'KZT',
    #     pg_ps_amount: 500,
    #     pg_ps_full_amount: 500,
    #     pg_ps_currency: 'KZT',
    #     pg_description:'Покупка в интернет магазине Site.kz',
    #     pg_result: 1,
    #     pg_payment_date: '2019-01-01 12:00:00',
    #     pg_can_reject: 1,
    #     pg_user_phone: 7077777777777,
    #     pg_user_contact_email: 'mail@customer.kz',
    #     pg_testing_mode: 1,
    #     pg_captured: 0,
    #     pg_card_pan: '5483-18XX-XXXX-0293',
    #     pg_salt: '123',
    #     pg_sig: '12',
    #     pg_payment_method: ''
    # }
    
    
    # key = f'init_payment.php;{pg_amount};{pg_description};{pg_merchant_id};{pg_order_id};{pg_salt};{secret_key}'
    # hash_object = hashlib.md5(key.encode('utf-8')).hexdigest()

    # data = {
    #     'pg_amount':pg_amount,
    #     'pg_description':pg_description,
    #     'pg_merchant_id':pg_merchant_id,
    #     'pg_order_id':pg_order_id,
    #     'pg_salt':pg_salt,
    #     'pg_sig': hash_object,
    # }

    # r = requests.post('https://api.paybox.money/init_payment.php', data=data)

    # print(r.text)

    return render(request, 'payment.html', {})
    
    
            
    

