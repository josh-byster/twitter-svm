from calculations import *
from getTweets import parse
import random
#MODIFY VARIABLES HERE
retrieveType="load" #should be load or save in quotes - should test set be loaded from memory or fetched new?
n_folds=10
parameters = {'kernel':['linear'],'C': [0.01,0.1,1,10,100]}
loadName='tweets600' #only matters if type is "load"
saveName='tweets1600' #only matters if type is "save"
channels=["nbcnews","foxnews","taylorswift13","mlb","nba","rihanna","twitter","jimmyfallon"]
n=500
pctTest=0.2
C=1
getFeatureWeights=True
shouldReturnMetrics=True
gridSearch=False
SVM=True
xValidate=False
shouldPredict=False

if(retrieveType=="load"):
    tweets=readFromMemory(loadName)
else:
    tweets=parse(channels,n)
    if(retrieveType=="save"):
        store(tweets,saveName)
print("Loaded " + str(len(tweets)) + " tweets.")
random.shuffle(tweets)

print(tweets[0].text + tweets[0].author)
vect_return,Y = split(tweets)
X=vect_return[1]
vectorizer=vect_return[0]
'''print(len(X[0]))
print(len(vectorizer.get_feature_names()))
for val in range(0,len(X[0])):
    if(X[0][val]==1):
        print vectorizer.get_feature_names()[val]
'''
if(gridSearch):
    gs(X,Y,folds,parameters)
if(SVM):
    svm=regularSVM(X,Y,C,pctTest,channels,shouldReturnMetrics)
    showCoefficients(svm,vectorizer,channels)
if(xValidate):
    crossValidate(X,Y,folds=n_folds,c=C)
if(shouldPredict):
    predictGame(svm,vectorizer)