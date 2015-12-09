from __future__ import absolute_import, print_function
import retrieve
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC,SVC
from sklearn import cross_validation
import sklearn
import numpy
from sklearn.externals import joblib
numpy.set_printoptions(threshold=numpy.nan)

args=retrieve.parse(["nbcnews","who","imdb"],2) #Returns tuple value in form (data,names) - number is in tuple form
vectorizer = CountVectorizer()
fit_array = numpy.array(vectorizer.fit_transform(args[0]).toarray())
X_train, X_test, y_train, y_test = cross_validation.train_test_split(fit_array, args[1], test_size=0.33)
joblib.dump(X_train,'Xtrain2.pkl')
joblib.dump(y_train,'Ytrain2.pkl')
joblib.dump(X_test,'Xtest2.pkl')
joblib.dump(y_test,'Ytest2.pkl')
#X_train=joblib.load('Xtrain.pkl')
#y_train=joblib.load("Ytrain.pkl")
#X_test=joblib.load("Xtest.pkl")
#y_test=joblib.load("Ytest.pkl")
print(X_train[5])
print(y_train)

clf = LinearSVC(C=100)
clf.fit(X_train,y_train)
pred_values=clf.predict(X_test[:1000])
for i in range(20,60):
    print(vectorizer.get_feature_names()[i])
    print(clf.coef_[0][i])
count_wrong=0
for i in range(0, len(pred_values)):
    if(pred_values[i]!=y_test[i]):
        print("Predicted: " + pred_values[i])
        print("Actual: " + y_test[i])
        count_wrong=count_wrong+1
        print(count_wrong)
print("Accuracy percentage: " + str(sklearn.metrics.accuracy_score(y_test[:1000], pred_values, normalize=True, sample_weight=None)))
#print("API requests remaining: " + str(args[2]))
print(pred_values)
print(y_test)
print(sklearn.metrics.confusion_matrix(y_test, pred_values, labels=None))


