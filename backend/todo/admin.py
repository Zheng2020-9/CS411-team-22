from django.contrib import admin
from .models import County, State

class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'state_name', 'stats')

# Register your models here.

admin.site.register(County, CountyAdmin)
admin.site.register(State)