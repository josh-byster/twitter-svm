# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:01:36 2015

@author: josbys1
"""
import re
import time
import pprint
from scipy import stats
import math
from credentials import keys
import tweepy
import numpy
import sys
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC,SVC
from sklearn.svm import SVC
from sklearn import cross_validation,metrics,grid_search
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

def readFromMemory(location):
    return joblib.load(location +'.pkl')
def store(tweets,location):
    joblib.dump(tweets,location+'.pkl')

def parse(channels,n):
    print("Getting tweets...")
    objList=[]
    for channel in channels:
        page = 1
        while page<=n:
            statuses = None
            try:
                statuses = api.user_timeline(page=page, id=channel)
            except:
                renew_time = time.strftime("%H:%M:%S", time.gmtime(api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['reset']-21600))
                sys.exit("Oops! Rate limit exceeded. Try again at: " + str(renew_time + " CST."))
            if statuses:
                for status in statuses:
                    txt = status["text"]
                    text_clean = re.sub(r"(?:\@|https?\:\/\/)\S+", "URL", txt)
                    newTweet = Tweet(text_clean,channel)
                    objList.append(newTweet)
            page += 1
            if(page%10==0):
                print(str(math.ceil(page/float(n) * 100)) + "% done with channel. " + "API calls left: " + str(api.rate_limit_status()['resources']['statuses']['/statuses/user_timeline']['remaining']))
        print("Moving on to next channel...")
    return objList

def getX(tweets):
    a=[]
    for obj in tweets:
        a.append(obj.text)
    return a

def getY(tweets):
    a=[]
    for obj in tweets:
        a.append(obj.author)
    return numpy.asarray(a)

def vectorize(tweets):
    vectorizer = CountVectorizer()
    ft = numpy.array(vectorizer.fit_transform(getX(tweets)).toarray())
    for i in range(0,len(tweets)-1):
        tweets[i].vector = ft[i]
    return ft


def split(tweets):
   return vectorize(tweets),getY(tweets)

def gs(X,Y,folds,parameters):
    cv=cross_validation.KFold(len(X), n_folds=folds,shuffle=True,random_state=None)
    svr = SVC()
    clf = grid_search.GridSearchCV(svr, parameters,cv=cv)
    clf.fit(X,Y)
    pprint.pprint(clf.grid_scores_)
    pprint.pprint(clf.best_params_)
def predict(x_test,model):
    return model.predict(x_test)

def getWrongValues(pred_values,y_test,percentage):
    count_wrong=0
    for i in range(0, len(pred_values)):
        if(pred_values[i]!=y_test[i]):
            print("Predicted: " + pred_values[i])
            print("Actual: " + y_test[i])
            count_wrong=count_wrong+1
            print(count_wrong)
    if(percentage):
        print("Accuracy percentage: " + str(metrics.accuracy_score(y_test, pred_values, normalize=True, sample_weight=None)))
        print(metrics.confusion_matrix(y_test, pred_values, labels=None))
