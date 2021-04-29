from django.db import models
from .state_db import states_init, counties_init
import csv
import urllib.request
import io


from django.contrib.auth.models import User


# Create your models here.
class County(models.Model):
    county_name = models.CharField(max_length=50, help_text='Name of a US County')
    state = models.CharField(max_length=40, help_text='Name of the US State that contains it')
    county_and_state = models.CharField(max_length=90, help_text='identifier', primary_key=True)
    fips = models.CharField(max_length=6, help_text='Assigned fips value (identifier)')
    cases = models.CharField(max_length=10, help_text='Number of COVID-19 cases')
    deaths = models.CharField(max_length=10, help_text='Number of COVID-19 deaths')

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
     State(name=state, fips=int(state_dict[state][0]), cases=int(state_dict[state][1]), deaths=int(state_dict[state][2])).save()

# update counties db
# COMMENT OUT IF RUNNING FOR THE FIRST TIME
county_db = counties_init()
for county in county_db:
    County(county_name=county_db[county][0], state=county_db[county][1], county_and_state=county, cases=county_db[county][2], deaths=county_db[county][3], fips=county_db[county][4]).save()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    org = models.CharField('Organization', max_length=128, blank=True)
 
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)
 
    class Meta:
        verbose_name = 'User Profile'
    
    def __str__(self):
        return "{}'s profile".format(self.user.__str__())
