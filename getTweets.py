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
    tweets=[getChannelTweets(ch,n) for ch in channels]
    return [item for sublist in tweets for item in sublist]
def getChannelTweets(channel,n,showRequestsRemaining=True):
    mx=None
    objList=[]
    while True:
        try:
            statuses = api.user_timeline(id=channel,count=200,max_id=mx)
            reqsLeft=api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['remaining']
        except:
            renew_time = time.strftime("%H:%M:%S", time.gmtime(api.rate_limit_status()['resources']
            ['statuses']['/statuses/user_timeline']['reset']-21600))
            sys.exit("Oops! Rate limit may have been exceeded. Try again at: " + str(renew_time + " CST."))
            print(sys.exc_info()[0])
        if statuses:
            for status in statuses:
                content = re.sub(r"(?:\@|https?\:\/\/)\S+", "URL", status["text"])
                newTweet = Tweet(content,channel)
                objList.append(newTweet)
                mx=status["id"]-1
                if(len(objList)==n):
                    if(showRequestsRemaining):
                        print(reqsLeft)
                    return objList
        else:
            return objList