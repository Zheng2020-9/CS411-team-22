from django.contrib import admin
from .models import County, State

class CountyAdmin(admin.ModelAdmin):
    list_display = ('county_name', 'state', 'cases', 'deaths')
    
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'fips', 'cases', 'deaths')


# Register your models here.

admin.site.register(County, CountyAdmin)
admin.site.register(State, StateAdmin)