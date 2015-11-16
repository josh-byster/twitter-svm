from __future__ import absolute_import, print_function

import parser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
numpy.set_printoptions(threshold=numpy.nan)

print(getTs("potus","who","imdb",10))
vectorizer = CountVectorizer()
fit_array = vectorizer.fit_transform(args).toarray()
print(fit_array)