import pandas as pd
import os
from sqlalchemy import create_engine


db_pass = os.environ.get('rich_m_pass')

engine = create_engine('mysql+pymysql://rich_m:' + db_pass + '@localhost:3306/sa_db')


def sent_a():
    """adds sentiment score data using a pandas dataframe converted from a local csv"""
    with open('news_api_20200514/sentiment_score.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql(name='sent_a', con=engine, index=True, index_label='id', if_exists='replace')


def headlines():
    """adds headline data using a pandas dataframe converted from a local csv"""
    with open('news_api_20200514/headlines2.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql(name="h_lines", con=engine, index=True, index_label='id', if_exists='replace')

#
def news():
    with open('news_api_20200514/news.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql("news", con=engine, index=True, index_label='id', if_exists='replace')

def yfin():
    with open('yfinance.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql(name="yfin", con=engine, index=True, index_label='id', if_exists='replace')


if __name__ == '__main__':
    sent_a()
    headlines()
    news()
    yfin()
