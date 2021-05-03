import csv
import urllib.request
import io

# csv_import: get a .csv file from url
def csv_import(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=',') 
    return csvfile

# states_init: creates a state/territory dictionary from NY Times
    # Dictionary configured as follows: 
    # key: state's name as string
    # value: a list containing the state's fips, cases, and deaths (as strings)
def states_init():
    db = csv_import('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv')
    state_dict = {}

    for row in db:
        state_dict[row[1]] = row[2:5]
    
    state_dict.pop('state', None)  # to remove header
    return state_dict 

# counties_init: creates a state/territory dictionary from NY Times
    # Dictionary configured as follows: 
    # key: county name + state name
    # value: a list containing the state's fips, cases, and deaths (as strings)
def counties_init():
    db = csv_import('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv')
    counties_dict = {}

    for row in db:
        name = row[1] + row[2]
        county = row[1]
        state = row[2]
        cases = row[4]
        deaths = row[5]
        if len(deaths) == 0:
            deaths = 'Unknown'
        
        counties_dict[name] = [county] + [state] + [cases] + [deaths]

    counties_dict.pop('countystate', None)  # to remove header
    return counties_dict