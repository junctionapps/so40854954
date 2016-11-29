from django.contrib import admin

# Register your models here.
from membership.models import CustomUser, CustomGroup, CustomSettings


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]


@admin.register(CustomSettings)
class CustomSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'group', 'user']
    pass
