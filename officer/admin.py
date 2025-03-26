from django.contrib import admin
from .models import Officers


class OfficerAdmin(admin.ModelAdmin):
    ordering = ['rank'] 


admin.site.register(Officers, OfficerAdmin)

