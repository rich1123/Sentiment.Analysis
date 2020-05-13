from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

######################
##  Load API Tokens
######################

tokenfile = open('/Users/psehgal/dev/Sentiment.Analysis/twitter_tokens.json')
tokens = json.load(tokenfile)
ckey = tokens['ckey']
csecret = tokens['csecret']
atoken = tokens['atoken']
asecret = tokens['asecret']

######################
##  Create listener class
######################

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

######################
##  main program
######################

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["$TSLA"])