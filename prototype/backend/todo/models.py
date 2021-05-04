from django.db import models
from .state_db import states_init, counties_init, county_vs_init, rolling_avg_init
import csv
import urllib.request
import io
import json

from django.contrib.auth.models import User


class County(models.Model):
    county_name = models.CharField(max_length=50, help_text='Name of a US County')
    state = models.CharField(max_length=40, help_text='Name of the US State that contains it')
    county_and_state = models.CharField(max_length=90, help_text='identifier', primary_key=True)
    fips = models.CharField(max_length=6, help_text='Assigned fips value (identifier)')
    cases = models.CharField(max_length=10, help_text='Number of COVID-19 cases')
    deaths = models.CharField(max_length=10, help_text='Number of COVID-19 deaths')
    vuln_score = models.CharField(max_length=7, help_text='Vulnerability score of the County')
    avg_cases = models.CharField(max_length=10, help_text='Average number of COVID-19 cases in the past week')
    avg_deaths = models.CharField(max_length=10, help_text='Average number of COVID-19 deaths in the past week')

    class Meta:
        ordering = ['state','county_name']

    def __str__(self):
        return self.county_name + " County, " + self.state

class State(models.Model):
    name = models.CharField(max_length=40, help_text='Name of a US state or territory')
    fips = models.IntegerField(help_text="Assigned fips value (unique identifier)", primary_key=True)
    cases = models.IntegerField(help_text='Number of COVID-19 cases')
    deaths = models.IntegerField(help_text='Number of COVID-19 deaths')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Userdata(models.Model):
    account = models.CharField(max_length = 15)
    pwd = models.CharField(max_length = 20)

# update state db
# COMMENT OUT IF RUNNING FOR THE FIRST TIME
state_dict = states_init()
for state in state_dict:
     State(name=state, \
           fips=int(state_dict[state][0]), \
           cases=int(state_dict[state][1]), \
           deaths=int(state_dict[state][2])\
     ).save()

# update counties db
# COMMENT OUT IF RUNNING FOR THE FIRST TIME
county_db = counties_init()
county_vuln_db = county_vs_init()
avg_db = rolling_avg_init()

for county in county_db:

    cases_val = county_db[county][2]
    deaths_val = county_db[county][3]
    try:
        case_death_ratio = float(deaths_val) / float(cases_val)
    except:
        case_death_ratio = 0.0

    try:
        vuln_val = str(round(float(county_vuln_db[county]) + (0.07 * case_death_ratio), 4))
    except KeyError:
        vuln_val = 'Unknown'

    try:
        avg_c = avg_db[county][0]
        avg_d = avg_db[county][1]
    except KeyError:
        avg_c = 'Unknown'
        avg_d = 'Unknown'

    County(county_name=county_db[county][0], \
           state=county_db[county][1], \
           county_and_state=county, \
           cases=cases_val, \
           deaths=deaths_val, \
           fips=county_db[county][4],\
           vuln_score=vuln_val,\
           avg_cases=avg_c, \
           avg_deaths=avg_d\
    ).save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    org = models.CharField('Organization', max_length=128, blank=True)
 
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)

    bookmarks = models.CharField(max_length=500,blank=True, default='25025')
 
    class Meta:
        verbose_name = 'User Profile'
    
    def __str__(self):
        return "{}'s profile".format(self.user.__str__())

    def add_bookmark(self, county):
        bookmark_list = self.bookmarks.split(',')
        
        if county not in bookmark_list:
            bookmark_list.append(county)

        self.bookmarks = joined_string = ",".join(bookmark_list)
        self.save()

    def delete_bookmark(self, county):
        bookmark_list = self.bookmarks.split(',')
        
        if county in bookmark_list:
            bookmark_list.remove(county)

        self.bookmarks = joined_string = ",".join(bookmark_list)
        self.save()

    def get_bookmarks(self):
        return self.bookmarks