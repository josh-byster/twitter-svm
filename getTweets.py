import re
import sys
import tweepy
import time
from credentials import keys
from TweetObj import Tweet
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
    print("Getting tweets...")
    objList=[]
    statuses = None
    tweetsReceived=0
    mx=None
    count=0
    for x in range(len(channels)):
        print("Iterating through next array: " + str(count))
        count=0
        channel=channels[x]
        while count<n:
            print("N: " + str(n))
            try:
                if(mx!=None):
                    statuses = api.user_timeline(id=channel,count=200,max_id=mx-1)
                    print("LENGTH OF STATUSES" + str(len(statuses)))
                else:
                    statuses = api.user_timeline(id=channel,count=200)
            except:
                renew_time = time.strftime("%H:%M:%S", time.gmtime(api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['reset']-21600))
                sys.exit("Oops! Rate limit exceeded. Try again at: " + str(renew_time + " CST."))
            if statuses:
                for status in statuses:
                    txt = status["text"]
                    text_clean = re.sub(r"(?:\@|https?\:\/\/)\S+", "URL", txt)
                    tweetsReceived+=1
                    print(text_clean)
                    count+=1
                    newTweet = Tweet(text_clean,channel)
                    objList.append(newTweet)
                    mx=status["id"]
                    if(tweetsReceived%100==0):
                        print(str(float(tweetsReceived)/n/len(channels)) + "% done. " + "API calls left: " + str(api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['remaining']))
                print(count)
    print("TOTAL TWEETS RECEIVED: " + str(tweetsReceived))
    return objList

