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

def parse(channels,n):
    x_values=[]
    y_values=[]
    for channel in channels:
        page = 1
        while page<=n:
            statuses = api.user_timeline(page=page, id=channel)
            if statuses:
                for status in statuses:
                    # process status here
                    x_values.append(status["text"])
                    y_values.append(channel)
                    print(status["text"])
            page += 1
    return (x_values,y_values,api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['remaining'])