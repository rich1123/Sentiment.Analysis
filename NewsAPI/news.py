import json
from newsapi import NewsApiClient
from datetime import date, timedelta
import os
import csv


# Init
newsapi = NewsApiClient(api_key='Enter Key Here')

path = os.path.join(os.path.dirname(__file__), 'news.csv')

# Delete CSV to overwrite
if os.path.exists(path):
	os.remove(path)


# Create new CSV with headers
with open(path,'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['date','total_articles'])


# Obtain article count per day for date range 
start = '2020-04-18'
end = '2020-05-18'

start2 = date(int(start[0:4]), int(start[5:7]), int(start[8:10]))
end2 = date(int(end[0:4]), int(end[5:7]), int(end[8:10]))
day = timedelta(days=1)

i = start2
while i <= end2:

	all_articles = newsapi.get_everything(q='Tesla',
	                                      from_param=i,
	                                      to=i,
	                                      language='en',
	                                      )

	with open(path, 'a') as f:
		f.write("{},{}\n".format(i.strftime('%Y-%m-%d'), all_articles["totalResults"]))

	i += day

