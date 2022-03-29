from warnings import filters
from django.contrib import admin
from .models import *


class NeedyAdmin(admin.ModelAdmin):
    list_filter = ('status', 'category', 'statusHome', 'region',)
    list_display = ('user', 'address', 'status', 'period', 'updated_at')
    
    def dublicate_ad(modeladmin, request, queryset):
        #клонирование выбранных Ad
        for ad in queryset:
            ad.pk = None
            ad.save()

    dublicate_ad.short_description = "Дублировать объект"   
    actions = [dublicate_ad]
    
class EventAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('user', 'type', 'cash', 'needy',)
    
    def dublicate_ad(modeladmin, request, queryset):
        #клонирование выбранных Ad
        for ad in queryset:
            ad.pk = None
            ad.save()

    dublicate_ad.short_description = "Дублировать объект"   
    actions = [dublicate_ad]

admin.site.register(Needy, NeedyAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(StatusType)
admin.site.register(StatusHome)
admin.site.register(Category)
admin.site.register(Region)
