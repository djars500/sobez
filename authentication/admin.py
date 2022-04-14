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
    list_filter = ('username', 'email', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username','name', 'surName' , 'image', )}),
        ('Permissions', {'fields': ('groups', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','name', 'surName', 'image','username', 'is_active', 'is_staff', 'is_superuser', 'groups' )}
        ),
    )
    search_fields = ('username',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)