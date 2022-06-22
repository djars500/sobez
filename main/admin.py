
import imp
from django.conf import settings
from django.contrib import admin
from .models import *
from django.contrib.gis.db.models import GeometryField
from django_admin_geomap import ModelAdmin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

class TabularInlineUser(admin.TabularInline):
    model = Needy
    readonly_fields = ('owner', 'changed_onwer')
    

class NeedyAdmin(ModelAdmin, admin.ModelAdmin):
    list_filter = ('status', 'category', 'statusHome',)
    list_display = ('user', 'address', 'status', 'period', 'updated_at',)
    readonly_fields = ('owner', 'changed_onwer')
    
    
    
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_latitude = "43.0401635"
    geomap_default_longitude = "69.3886292"
    geomap_default_zoom = "14"
    geomap_item_zoom = "15"
    geomap_height = "600px"
    
    def dublicate_ad(modeladmin, request, queryset):
        #клонирование выбранных Ad
        for ad in queryset:
            ad.pk = None
            ad.save()

    dublicate_ad.short_description = "Дублировать объект"   
    
    my_id_for_formfield = None
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.my_id_for_formfield = obj.id
        return super(NeedyAdmin, self).get_form(request, obj, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            try:
                kwargs["queryset"] = User.objects.filter(groups__name__in=['Мұқтаж',])
            except Family.DoesNotExist:
                print('error')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
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


class FamilyAdmin(AjaxSelectAdmin ,ModelAdmin,admin.ModelAdmin ):
    inlines = [
        TabularInlineUser,
    ]
    list_display = ('id',)

    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_latitude = "43.0401635"
    geomap_default_longitude = "69.3886292"
    geomap_default_zoom = "14"
    geomap_item_zoom = "15"
    geomap_height = "600px"
    
 
    
    my_id_for_formfield = None
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.my_id_for_formfield = obj.id
        return super(FamilyAdmin, self).get_form(request, obj, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_family":
            try:
                kwargs["queryset"] = Family.objects.get(id=self.my_id_for_formfield).needy_family.all()
            except Family.DoesNotExist:
                print('error')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        
      
        obj.lat = obj.main_family.lat
        obj.lon = obj.main_family.lon
        print('ok')
        print(obj.needy_family.all())
        
        
        super(FamilyAdmin, self).save_model(request, obj, form, change)

admin.site.register(Needy, NeedyAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Family, FamilyAdmin)
