from calculations import *

#MODIFY VARIABLES HERE
retrieveType="load" #should be load or save in quotes - should test set be loaded from memory or fetched new?
folds=10
parameters = {'kernel':['linear'],'C': [0.01,0.1,1,10, 100, 1000]}
loadName='tweets1k' #only matters if type is "load"
saveName='tweets2k' #only matters if type is "save"
channels=["nbcnews","who","barackobama","taylorswift13","abcnews"]
pages=10
pctTest=0.33
C=100
getFeatureWeights=True
shouldReturnMetrics=True
if(retrieveType=="load"):
    tweets=readFromMemory(loadName)
else:
    tweets=parse(channels,pages)
    if(retrieveType=="save"):
        store(tweets,saveName)

vect_return,Y = split(tweets)
X=vect_return[1]
vectorizer=vect_return[0]
print(vectorizer)
#gs(X,Y,folds,parameters)
svm=regularSVM(X,Y,C,pctTest,getFeatureWeights,channels,shouldReturnMetrics)
predictGame(svm,vectorizer)