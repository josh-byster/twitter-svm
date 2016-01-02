from __future__ import absolute_import, print_function
from retrieve import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC,SVC
from sklearn.svm import SVC
from sklearn import cross_validation,metrics
import numpy
from sklearn.externals import joblib
numpy.set_printoptions(threshold=numpy.nan)

#MODIFY VARIABLES HERE
retrieveMemory=False
overwriteMemory=False
channels=["nbcnews","who","imdb"]
pages=1
split_ratio=0.33
C=100
shouldReturnAccuracy=True
    
tweets=parse(channels,pages) 
X_train, X_test, y_train, y_test = split(tweets,split_ratio)
model=fit(X_train,y_train,C)
predicted_vals=predict(X_test,model)
getWrongValues(predicted_vals,y_test,shouldReturnAccuracy)



