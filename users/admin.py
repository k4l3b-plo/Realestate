from django.contrib import admin
from django.db import models
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'name',)
    list_filter = ('email', 'name', 'is_active', 'is_staff')
    ordering = ('-joined_date',)
    list_display = ('email', 'name',
                    'is_active', 'is_staff', 'is_Realtor')
    fieldsets = (
        (None, {'fields': ('email', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_Realtor')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)