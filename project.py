from calculations import *
from getTweets import parse
import random
import time
import datetime
#MODIFY VARIABLES HERE
retrieveType="load" #should be load or save in quotes - should test set be loaded from memory or fetched new?
n_folds=10
parameters = {'kernel':['linear'],'C': [0.01,0.1,1,10,100]}
loadName='tweets1000' #only matters if type is "load"
saveName='newscomp' #only matters if type is "save"
channels=["jimmykimmel","cbsnews","nbcnews","shakira"]
n=600
pctTest=0.2
C=1
getFeatureWeights=True
shouldReturnMetrics=True
gridSearch=False
SVM=True
showCoef=True
xValidate=False
shouldPredict=True
shouldTestOverN=False

start=time.time()
if(retrieveType=="load"):
    tweets=readFromMemory(loadName)
else:
    tweets=parse(channels,n)
    if(retrieveType=="save"):
        store(tweets,saveName)
print("Loaded " + str(len(tweets)) + " tweets.")
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
        showCoefficients(svm,vectorizer)
if(xValidate):
    crossValidate(X,Y,folds=n_folds,c=C)
if(shouldPredict):
    predictTweet(svm,vectorizer)
if(shouldTestOverN):
    testOverN(X,Y,C,pctTest,channels)

print("Total runtime: " + str(datetime.timedelta(seconds=round(time.time()-start,2))))