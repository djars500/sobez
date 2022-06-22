from tokenize import group
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email',  'is_superuser')
    list_filter = ('email', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'surName' , 'image', )}),
        ('Permissions', {'fields': ('groups', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','name', 'surName', 'image', 'is_active', 'is_staff', 'is_superuser', 'groups' )}
        ),
    )
    list_display_links = ('username', 'email',)
    search_fields = ('username',)
    ordering = ('email',)
    
    
    
    def save_model(self, request, obj, form, change):
        print(obj.username)
        if obj.username is None:
            print('work')
            obj.username = f'{obj.surName} {obj.name}'
        
        super(CustomUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(User, CustomUserAdmin)