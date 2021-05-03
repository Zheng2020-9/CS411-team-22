from django.db import models
from .state_db import states_init
import csv
import urllib.request
import io

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=40, help_text='Name of a US state or territory')
    fips = models.IntegerField(help_text="Assigned fips value (unique identifier)", primary_key=True)
    cases = models.IntegerField(help_text='Number of COVID-19 cases')
    deaths = models.IntegerField(help_text='Number of COVID-19 deaths')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class County(models.Model):
    name  = models.CharField(max_length=50, help_text='Name of a US county')
    state = models.CharField(max_length=40, help_text='Name of a US state or territory')
    name_state = models.CharField(max_length=90, help_text='Name of a US state or territory', primary_key=True)
    cases = models.IntegerField(help_text='Number of COVID-19 cases')
    deaths = models.IntegerField(help_text='Number of COVID-19 deaths')

# update state db
state_dict = states_init()
for state in state_dict:
    State(name=state, fips=int(state_dict[state][0]), cases=int(state_dict[state][1]), deaths=int(state_dict[state][2])).save()