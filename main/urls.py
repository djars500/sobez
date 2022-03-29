from django.urls import path
from .views import NeedyList, NeedyListDetail, EvenList, main

urlpatterns = [
    path('main/', main, name='main'),
    path('', NeedyList, name="needy_list"),
    path('detail/', NeedyListDetail, name="needy_list_detail"),
    path('event/', EvenList, name="event_list"),
]
