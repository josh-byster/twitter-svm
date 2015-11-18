from __future__ import absolute_import, print_function
from parser import process_tweets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import cross_validation
import numpy
numpy.set_printoptions(threshold=numpy.nan)

args=process_tweets("potus","who","imdb",10) #Returns tuple value in form (data,names)
vectorizer = CountVectorizer()
fit_array = numpy.array(vectorizer.fit_transform(args[0]).toarray())
X_train, X_test, y_train, y_test = cross_validation.train_test_split(fit_array, args[1], test_size=0.33, random_state=42)
