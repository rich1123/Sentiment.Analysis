import numpy as np
import pandas as pd
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Load headlines2.csv
path2 = os.path.join(os.path.dirname(__file__),'headlines2.csv')
df_headlines = pd.read_csv(path2)

# Create empty column to store sentiment scores per article
df_headlines['score'] = np.nan


# Tokenize essentially splits a sentence into words
headline_0 = word_tokenize(df_headlines['headline'][0])


# Stop words are words that provide no sentiment meaning
stop_words = stopwords.words('english')


# Append ':' to stop_words list
stop_words.append(':')


# Load Vader Lexicon
sid = SentimentIntensityAnalyzer()


# Iterate through df_headlines to determine sentiment score for each headline
for index, row in df_headlines.iterrows():
    headline_tokenized = word_tokenize(row['headline'])
    filtered_headline = []
    for word in headline_tokenized:
        if word not in stop_words:
            filtered_headline.append(word)
    #print(filtered_headline)
    headline_pos = []
    headline_neg = []
    headline_neu = []
    for word in filtered_headline:
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            headline_pos.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            headline_neg.append(word)
        else:
            headline_neu.append(word)
    
    score = round((1*len(headline_pos) - 1*len(headline_neg) + 0*len(headline_neu))/len(filtered_headline),2)
    df_headlines.at[index,'score'] = score


# Create a copy of df_headlines to perform grouping operations
df_headlines2 = df_headlines.copy()
df_headlines2.drop(['source', 'headline'], axis=1, inplace=True)


# Group headlines by date and calculate average score
df_group = df_headlines2.groupby('date').mean()
df_group.rename(columns = {'score': 'daily_score'}, inplace = True)


# Save df_group to csv
df_group.to_csv(os.path.join(os.path.dirname(__file__),'sentiment.csv'))


