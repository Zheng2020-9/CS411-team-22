import csv
import urllib.request
import io
from datetime import date, timedelta

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
        fips = row[3]
        cases = row[4]
        deaths = row[5]
        if len(deaths) == 0:
            deaths = 'Unknown'
        
        counties_dict[name] = [county] + [state] + [cases] + [deaths] + [fips]

    counties_dict.pop('countystate', None)  # to remove header
    return counties_dict

def rolling_avg_init():
    db = csv_import('https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-counties-recent.csv')
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    rolling_dict = {}

    for row in db:
        if row[0] != str(yesterday):
            continue
        state_county = row[2] + row[3]
        rolling_dict[state_county] = [row[5]] + [row[8]]
    
    return rolling_dict

def county_vs_init():
    yesterday = date.today() - timedelta(days=1)
    url = 'https://raw.githubusercontent.com/COVID19PVI/data/master/Model11.2.1/Model_11.2.1_' + yesterday.strftime('%Y%m%d') + '_results.csv'
    db = csv_import(url)
    county_score_dict = {}

    for row in db:
        state_county = row[3]
        if state_county == 'Name':
            continue
    
        splitup = state_county.split(", ")
        name = splitup[1] + splitup[0]

        index_val = str( \
                    round (float(row[5]) * 0.2  + \
                    float(row[6])  * 0.03 + \
                    float(row[7])  * 0.07 + \
                    float(row[8])  * 0.08 + \
                    float(row[9])  * 0.08 + \
                    float(row[10]) * 0.07 + \
                    float(row[11]) * 0.04 + \
                    float(row[12]) * 0.08 + \
                    float(row[13]) * 0.08 + \
                    float(row[14]) * 0.08 + \
                    float(row[15]) * 0.08 + \
                    float(row[16]) * 0.04 , 4)  \
                    )

        county_score_dict[name] = index_val
        # iden = name + " has a val of: " + index_val
        # print(iden)

    return county_score_dict