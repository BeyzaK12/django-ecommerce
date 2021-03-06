from django.contrib import admin

from .models import Ürün, Öne_Çıkanlar_Ürün

from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'phone_number', 'kimlik_numarası', 'vergi_numarası', 'first_name',
                    'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'phone_number', 'kimlik_numarası', 'vergi_numarası', 'first_name',
                   'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('phone_number', 'kimlik_numarası', 'vergi_numarası', 'first_name',
                                    'last_name', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number', 'kimlik_numarası', 'vergi_numarası', 'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'phone_number',
                     'kimlik_numarası', 'vergi_numarası')
    ordering = ('email', 'phone_number', 'kimlik_numarası', 'vergi_numarası')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ürün)
admin.site.register(Öne_Çıkanlar_Ürün)
