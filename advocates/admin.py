from django.contrib import admin
from .models import Language, Area, Advocate, Role, AdvocateRole


class AdvocateRoleAdmin(admin.ModelAdmin):
    ordering = ['appointed_on'] 


class AdvocateAdmin(admin.ModelAdmin):
    ordering = ['name'] 

admin.site.register(Language)
admin.site.register(Area)
admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Role)
admin.site.register(AdvocateRole, AdvocateRoleAdmin)

