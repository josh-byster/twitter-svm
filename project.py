from __future__ import absolute_import, print_function
from calculations import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC,SVC
from sklearn.svm import SVC
from sklearn import cross_validation,metrics
import numpy
from sklearn.externals import joblib
numpy.set_printoptions(threshold=numpy.nan)

#MODIFY VARIABLES HERE
retrieveType="none" #should be load or save in quotes - should test set be loaded from memory or fetched new?
loadName='tweets' #only matters if type is "load"
saveName='tweets20' #only matters if type is "save"
channels=["nbcnews","who","barackobama"]
pages=1
split_ratio=0.33
C=100
shouldReturnMetrics=True
if(retrieveType=="load"):
    tweets=readFromMemory(loadName)
else:
    tweets=parse(channels,pages)
    if(retrieveType=="save"):
        store(tweets,saveName)

X,Y = split(tweets)
x_validate(X,Y,10,C)


