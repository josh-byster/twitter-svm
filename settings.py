#MODIFY VARIABLES HERE
n_folds=10
parameters = {'kernel':['linear'],'C': [0.01,0.1,1,10,100]}
#channels=["katyperry","BarackObama","YouTube","TheEllenShow","twitter","instagram","cnnbrk","oprah","espn","sportscenter","pitbull","nba","kanyewest","nfl","chrisbrown"]
channels=["rihanna","nba"]
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
