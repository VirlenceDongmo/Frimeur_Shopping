from django.contrib import admin
from .models import CustomUser, Profile


class CustomUserAdmin(admin.ModelAdmin) :

    list_display = ('nom', 'prenom', 'email', 'is_superuser',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin) :

    list_display = ('user', 'birthday',)


admin.site.register(CustomUser, CustomUserAdmin)
