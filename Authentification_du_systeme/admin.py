from django.contrib import admin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin) :

    list_display = ('email','is_superuser', 'is_staff', 'is_active',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin) :

    list_display = ('user', 'birthday',)
