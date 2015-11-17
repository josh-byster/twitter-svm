# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:01:36 2015

@author: josbys1
"""
import re
from credentials import keys
import tweepy
import numpy
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


def process_tweets(channel1,channel2,channel3,n):
    tweets_src_one=api.user_timeline(channel1,count=n) #Test Twitter channels
    tweets_src_two=api.user_timeline(channel2,count=n)
    tweets_src_three=api.user_timeline(channel3,count=n)
    raw_tweets=[]
    stripped_tweets=[]
    names=[]
    def appendToRaw(arr,name):
        for i in range(0,len(arr)):
            raw_tweets.append(arr[i])
            names.append(name)
    appendToRaw(tweets_src_one,channel1)
    appendToRaw(tweets_src_two,channel2)
    appendToRaw(tweets_src_three,channel3)
    print names
    for obj in raw_tweets:
        #print(obj["text"])
        text=re.sub(r"(?:\@|https?\://)\S+", '', obj["text"], flags=re.MULTILINE)
        stripped_tweets.append(text)
    return stripped_tweets

