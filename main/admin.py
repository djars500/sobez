from dataclasses import fields
from warnings import filters
from django.contrib import admin
from .models import *


class TabularInlineUser(admin.TabularInline):
    model = Needy

class NeedyAdmin(admin.ModelAdmin):
    list_filter = ('status', 'category', 'statusHome',)
    list_display = ('user', 'address', 'status', 'period', 'updated_at')
    readonly_fields = ('owner', 'changed_onwer')
    def dublicate_ad(modeladmin, request, queryset):
        #клонирование выбранных Ad
        for ad in queryset:
            ad.pk = None
            ad.save()

    dublicate_ad.short_description = "Дублировать объект"   
    actions = [dublicate_ad]
    
    def save_model(self, request, obj, form, change):
        if obj.owner is None:     
            obj.owner = request.user
        else:
            obj.changed_onwer = request.user
        super(NeedyAdmin, self).save_model(request, obj, form, change)
    
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


class FamilyAdmin(admin.ModelAdmin):
    inlines = [
        TabularInlineUser,
    ]
    list_display = ('id',)
    
    my_id_for_formfield = None
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.my_id_for_formfield = obj.id
        return super(FamilyAdmin, self).get_form(request, obj, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_family":
            
            kwargs["queryset"] = Family.objects.get(id=self.my_id_for_formfield).needy_family.all()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Needy, NeedyAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Family, FamilyAdmin)
