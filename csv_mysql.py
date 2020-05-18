import pandas as pd
import pymysql
import csv
import os
from sqlalchemy import create_engine
import sqlalchemy


db_pass = os.environ.get('rich_m_pass')

engine = create_engine('mysql+pymysql://rich_m:' + db_pass + '@localhost:3306/sa_db')


def sent_a():
    # df = pd.read_csv('/news_api_20200514/sentiment_score.csv', delimiter=',')
    # df.to_sql(name="sent_a", con=conn, if_exists='replace')
    with open('news_api_20200514/sentiment_score.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql(name='sent_a', con=engine, index=True, index_label='id', if_exists='replace')


def headlines():
    # conn = create_engine('mysql://rich:db_pass@localhost:3306/sa_db'
    with open('news_api_20200514/headlines2.csv', 'r') as file:
        df = pd.read_csv(file)
    # df = pd.read_csv('news_api_20200514/headlines2.csv', delimiter=',')
    df.to_sql(name="h_lines", con=engine, if_exists='replace')

#
def news():
    # conn = create_engine('mysql://rich:db_pass@localhost:3306/sa_db')
    with open('news_api_20200514/news.csv', 'r') as file:
        df = pd.read_csv(file)
    df.to_sql("news", con=engine, if_exists='replace', index=False)

# def yfin():
#     df = pd.read_csv('/.csv', delimiter=',')
#     df.to_sql(name="qb", con=conn, if_exists='replace')


if __name__ == '__main__':
    sent_a()
    headlines()
    news()
