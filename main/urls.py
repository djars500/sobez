from django.urls import path
from .views import NeedyList, NeedyListDetail, EvenList, main, NeedyListDetailInfo, NeedyFamilyList, NeedyFamilyInfo, payment

urlpatterns = [
    path('main/', NeedyList, name='needy_list'),
    path('', main, name="main"),
    path('detail/', NeedyListDetail, name="needy_list_detail"),
    path('event/', EvenList, name="event_list"),
    path('detail/<int:pk>', NeedyListDetailInfo, name="needy_info"),
    path('family_list', NeedyFamilyList, name="needy_family_list"),
    path('family_detail/<int:pk>', NeedyFamilyInfo, name="family_detail"),
    path('payment/', payment, name='payment' )
 
]
