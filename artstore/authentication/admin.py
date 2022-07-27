from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'last_login', 'is_active',)
    list_display_links = ('id', 'username',)
    list_filter = ('last_login',)


admin.site.register(Users, UsersAdmin)
