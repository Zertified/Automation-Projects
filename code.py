from requests import get
import json
import datetime
import tkinter
import matplotlib.pyplot as plt

x = datetime.datetime.now()


cases = list()
dates = list()

def get_data(url):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

endpoint = (
'https://api.coronavirus.data.gov.uk/v1/data?'
'filters=areaType=nation;areaName=england&'
'structure={"date":"date","newCases":"newCasesByPublishDate"}'
)
    
data = get_data(endpoint)

today = str(datetime.datetime.now())

now = today[0:10]

for p in data['data']:
	cases.append(p['newCases'])

	dates.append(now)
	





today = str(datetime.datetime.now())


print("Date: "+now)

daily_date = dates.index(now)

print("Cases today: "+str(cases[daily_date]))

plottable_cases = list()
plottable_dates = list()

plottable_cases.append(cases[daily_date])
plottable_dates.append(now)

plt.plot(plottable_cases,plottable_dates,'ro')

plt.ylabel("Dates of when Covid Cases occured ")

plt.xlabel("Amount of Cases")

plt.title("A graph showing the amount of Covid Cases daily.")

plt.show()






