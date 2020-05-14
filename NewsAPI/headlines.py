import json
from newsapi import NewsApiClient
from datetime import date, timedelta
import os
import csv
import pandas as pd
import time


# Init
newsapi = NewsApiClient(api_key='Enter your key here')


# Delete CSV to overwrite
if os.path.exists('headlines.csv'):
	os.remove('headlines.csv')


# Create new CSV with headers
with open('headlines.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['date', 'source', 'headline'])


# Obtain article count per day for date range 
start = '2020-04-12'
end = '2020-05-12'

start2 = date(int(start[0:4]), int(start[5:7]), int(start[8:10]))
end2 = date(int(end[0:4]), int(end[5:7]), int(end[8:10]))
day = timedelta(days=1)

i = start2
while i <= end2:

	all_articles = newsapi.get_everything(q='Tesla',
										  sources='Bloomberg,CNBC',
	                                      from_param=i,
	                                      to=i,
	                                      language='en',
	                                      )

	with open('headlines.csv', 'a') as f:
		for x in all_articles['articles']:
			f.write("{},{},{}\n".format(i.strftime('%Y-%m-%d'), x['source']['name'], x['title']))

	i += day


# Concatenate columns
path = os.path.join(os.path.dirname(__file__),'headlines.csv')
path2 = os.path.join(os.path.dirname(__file__),'headlines2.csv')

with open(path, 'r') as f, open(path2, 'w') as g:
	reader = csv.reader(f)
	next(reader) # Skip the header
	writer = csv.writer(g)
	writer.writerow(['date', 'source', 'headline', 'hd', 'he', 'hf', 'hg', 'hh']) # Write the header

	for row in reader:
		# Remove white spaces in each field and assign to vars
		date, source, headline, hd, he, hf, hg, hh = [x.strip() for x in row]
		writer.writerow([date, source, headline + ' ' + hd + ' ' + he + ' ' + hf + ' ' + hg + ' ' + hh])


