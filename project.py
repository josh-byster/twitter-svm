from __future__ import absolute_import, print_function
from parser import process_tweets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import numpy
numpy.set_printoptions(threshold=numpy.nan)

args=process_tweets("potus","who","imdb",10)
vectorizer = CountVectorizer()
fit_array = vectorizer.fit_transform(args).toarray()
print(fit_array)