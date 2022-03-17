
from django.contrib import admin

from userapp.models import PostUser


@admin.register(PostUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name']
