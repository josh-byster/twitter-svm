from __future__ import absolute_import, print_function
import parser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import cross_validation
import sklearn
import numpy
import pandas as pd
numpy.set_printoptions(threshold=numpy.nan)

args=parser.parse(["nbcnews","who","imdb"],2) #Returns tuple value in form (data,names) - number is in tuple form
vectorizer = CountVectorizer()
fit_array = numpy.array(vectorizer.fit_transform(args[0]).toarray())
X_train, X_test, y_train, y_test = cross_validation.train_test_split(fit_array, args[1], test_size=0.33, random_state=42)
clf = SVC(gamma=0.001,C=100)
clf.fit(X_train,y_train)
pred_values=clf.predict(X_test[:1000])
count_wrong=0
for i in range(0, len(pred_values)):
    if(pred_values[i]!=y_test[i]):
        print("Predicted: " + pred_values[i])
        print("Actual: " + y_test[i])
        count_wrong=count_wrong+1
        print(count_wrong)
print("Accuracy percentage: " + str(sklearn.metrics.accuracy_score(y_test[:1000], pred_values, normalize=True, sample_weight=None)))
print("API requests remaining: " + str(args[2]))
print(pred_values)
print(y_test)
print(sklearn.metrics.confusion_matrix(y_test, pred_values, labels=None))


