from __future__ import absolute_import, print_function

import tweepy
from credentials import keys
import json
import numpy
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
numpy.set_printoptions(threshold=numpy.nan)
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=keys["consumer_key"]
consumer_secret=keys["consumer_secret"]

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=keys["oauth_token"]
access_token_secret=keys["oauth_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

n = 100
tweets_src_one=api.user_timeline("who",count=n) #Test Twitter channels
tweets_src_two=api.user_timeline("potus",count=n)
tweets_src_three=api.user_timeline("twitter",count=n)
raw_tweets=[]
stripped_tweets=[]
def appendToRaw(arr):
    for i in range(0,len(arr)):
        raw_tweets.append(arr[i])
appendToRaw(tweets_src_one)
appendToRaw(tweets_src_two)
appendToRaw(tweets_src_three)
for obj in raw_tweets:
    #print(obj["text"])
    text=re.sub(r"(?:\@|https?\://)\S+", '', obj["text"], flags=re.MULTILINE)
    stripped_tweets.append(text)
#print(tweet_array)
vectorizer = CountVectorizer()
fit_array = vectorizer.fit_transform(stripped_tweets).toarray()
#print(fit_array)

