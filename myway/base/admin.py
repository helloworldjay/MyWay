from django.contrib import admin
from .models import User_info
# Register your models here.

@admin.register(User_info)
class User_infoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo', 'is_fhp']

