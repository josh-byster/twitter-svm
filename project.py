from __future__ import absolute_import, print_function
from parser import getTweets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import cross_validation
import sklearn
import numpy
numpy.set_printoptions(threshold=numpy.nan)

args=getTweets(["nbcnews","who","imdb"],10) #Returns tuple value in form (data,names) - number is in tuple form
print(args[0])
print(args[1])
vectorizer = CountVectorizer()
fit_array = numpy.array(vectorizer.fit_transform(args[0]).toarray())
X_train, X_test, y_train, y_test = cross_validation.train_test_split(fit_array, args[1], test_size=0.33, random_state=42)
clf = SVC(gamma=0.001,C=100)
clf.fit(X_train,y_train)
pred_values=clf.predict(X_test[:1000])
for i in range(0, len(pred_values)):
    print("Predicted: " + pred_values[i])
    print("Actual: " + y_test[i])
print(sklearn.metrics.accuracy_score(y_test[:1000], pred_values, normalize=True, sample_weight=None))