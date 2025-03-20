from django.contrib import admin

from .models import *  
# Register your models here.

@admin.register(Momo)
class MomoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','image', 'price')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'message')