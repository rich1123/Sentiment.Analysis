# Sentiment.Analysis
Our chosen topic is Sentiment Analysis regarding its effect on publicly traded stock. We will be monitoring daily summed mentions on identified stocks, from Twitter, to see if any correlation can be acknowledged between this and their stock price. 

Using Airflow and Python, we will use the Yahoo Finance API to keep up to date on price changes (opening and closing daily).

Data obtained from each source will be stored into a SQL database.

We will use Apache Spark to wrangle the data. We will then push the cleaned data into a new SQL database.

We will connect Jupyter to SQL to load the data. We will then use matplotlib to plot said data.
![](images/Sentiment_Analysis_Social_Media_Stock.png)
