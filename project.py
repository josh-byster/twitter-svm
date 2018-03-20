from calculations import *
from getTweets import parse
import random
import time
import datetime
from settings import *

shouldLoad=input("Would you like to load an existing dataset? ")
if(shouldLoad=="yes"):
    loadName=input("What's the name of the file you would like to load? ")
    tweets=readFromMemory(loadName)
elif(shouldLoad=="no"):
    print("OK, now parsing channels in the settings file...")
    tweets=parse(channels,n)
    shouldSave=input("Would you like to save this dataset?")
    if(shouldSave=="yes"):
        saveName=input("Please name the dataset file: ")
        store(tweets,"data/"+saveName)
try:
    print("Loaded " + str(len(tweets)) + " tweets.")
except NameError:
    print("You did not enter a valid input.")
start=time.time()
random.shuffle(tweets)
vect_return,Y = split(tweets)
#numpy.random.shuffle(Y)
X=vect_return[1]
vectorizer=vect_return[0]
if(gridSearch):
    gs(X,Y,folds,parameters)
if(SVM):
    svm=regularSVM(X,Y,C,pctTest,shouldReturnMetrics)
    if(showCoef):
        if(len(svm.classes_)!=2):
            showCoefficients(svm,vectorizer)
            print(len(svm.classes_))
        else:
            print("Note that this is a binary classification")
            showBinaryCoefs(svm,vectorizer)
if(xValidate):
    crossValidate(X,Y,folds=n_folds,c=C)
if(shouldPredict):
    predictTweet(svm,vectorizer)
if(shouldTestOverN):
    testOverN(X,Y,C,pctTest,channels)

print("Total runtime: " + str(datetime.timedelta(seconds=round(time.time()-start,2))))