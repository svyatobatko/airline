from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'created_at', 'updated_at')


admin.site.register(User, UserAdmin)
