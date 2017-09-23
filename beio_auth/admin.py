# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from beio_auth.models import BeioUser
from beio_auth.forms import BeioUserCreationForm,BeioPasswordRestForm,BeioChangeUserForm


# Register your models here.

class BeioUserAdmin(UserAdmin):
    add_form = BeioUserCreationForm
    # form=BeioChangeUserForm
    list_display=('username', 'email', 'date_of_birth','createdate')
    list_filter=('is_admin',)
    fieldsets = (
        (u'基本信息', {'fields': ('username', 'password', 'email','date_of_birth')}),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_admin')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields=('email',)
    ordering=('createdate',)
    filter_horizontal = ()
# 
admin.site.register(BeioUser, BeioUserAdmin)
admin.site.unregister(Group)
# admin.site.register(BeioUser)
