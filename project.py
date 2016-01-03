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
retrieveType="load" #should be load or save in quotes - should test set be loaded from memory or fetched new?
loadName='tweets' #only matters if type is "load"
saveName='tweets' #only matters if type is "save"
channels=["nbcnews","who","imdb"]
pages=45
split_ratio=0.33
C=100
shouldReturnMetrics=True

if(retrieveType=="load"):
    tweets=readFromMemory(loadName)
if(retrieveType=="save"):
    tweets=parse(channels,pages)
    if(saveTestSet):
        store(tweets,saveName)

X_train, X_test, y_train, y_test = split(tweets,split_ratio)
model=fit(X_train,y_train,C)
predicted_vals=predict(X_test,model)
getWrongValues(predicted_vals,y_test,shouldReturnMetrics)



