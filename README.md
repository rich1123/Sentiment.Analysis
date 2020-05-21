# Sentiment.Analysis
Our chosen topic is Sentiment Analysis regarding its effect on publicly traded stock. We will be monitoring daily summed mentions on identified stocks, from Twitter as wells as collected headlines from NewsAPI, to see if any correlation can be acknowledged between this and their stock price. 

Using Airflow and Python, we will use the Yahoo Finance API to keep up to date on price changes (opening and closing daily).

Data obtained from Twitter and NewsAPI will be converted to CSVs. 

Data from Yfinance will be added to our database via 

This data will be stored in a SQL database, with a Python script using sqlalchemy, as a lake for future considerations and store for the current analysis.  

![](images/Sentiment_Analysis_Social_Media_Stock.png) 
