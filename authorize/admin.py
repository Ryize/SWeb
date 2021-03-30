from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'created_at', 'is_publiced')
    list_display_links = ('id', 'login', 'email', 'created_at', 'is_publiced')
    search_fields = ('id', 'login', 'email')

admin.site.register(User, UserAdmin)