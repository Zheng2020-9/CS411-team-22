from django.contrib import admin
from .models import County, State, UserProfile

class CountyAdmin(admin.ModelAdmin):
    list_display = ('county_name', 'state', 'fips' , 'cases', 'deaths', 'vuln_score', 'avg_cases', 'avg_deaths')

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'fips', 'cases', 'deaths')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'org', 'telephone', 'mod_date', 'bookmarks')


# Register your models here.

admin.site.register(County, CountyAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(UserProfile, UserProfileAdmin)