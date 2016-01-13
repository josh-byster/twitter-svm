from __future__ import absolute_import, print_function
from calculations import *
import numpy
numpy.set_printoptions(threshold=numpy.nan)

#MODIFY VARIABLES HERE
retrieveType="load" #should be load or save in quotes - should test set be loaded from memory or fetched new?
folds=10
parameters = {'kernel':['linear'],'C': [0.01,0.1,1,10, 100, 1000]}
loadName='tweets1k' #only matters if type is "load"
saveName='tweets1k' #only matters if type is "save"
channels=["nbcnews","who","barackobama","taylorswift13","abcnews"]
pages=6
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

X,Y = split(tweets)
#gs(X,Y,folds,parameters)
regularSVM(X,Y,C,pctTest,getFeatureWeights,shouldReturnMetrics)
