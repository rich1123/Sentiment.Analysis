# Sentiment.Analysis
Our chosen topic is Sentiment Analysis regarding its effect on publicly traded stock. We will be monitoring daily summed mentions on identified stocks, from Twitter (https://developer.twitter.com/en/docs), and Headline totals gathered from NewsAPI(https://newsapi.org/) to see if any correlation can be acknowledged between this and their stock price. 

Using Airflow and Python, we will use the Yahoo Finance API (https://pypi.org/project/yfinance/) to keep up to date on price changes (opening and closing daily).

Data obtained from each source will be stored into a MYSQL database.

We will connect Jupyter to SQL to load the data. We will then use bokeh to plot said data and a correlation matrix to evaluate our process.
![](images/Sentiment_Analysis_Social_Media_Stock.png) 
