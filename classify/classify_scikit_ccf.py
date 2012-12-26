import sklearn.svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import numpy
import sklearn.cross_validation
from sklearn.feature_selection.selector_mixin import SelectorMixin
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import LeaveOneOut
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import sys


def dostuff(k_val):
    
    feats = []
    labels = []
    
    for line in open(sys.argv[1]): #open("sex01.csv"):
        line = line.strip(" \n")
        arr = line.split(",") 
        labels.append(int(float(arr[0])))
        feature = [ float(x) for x in arr[1:] ]
        feats.append(feature)
    
    
    y = numpy.array(labels)
    X = numpy.array(feats)
    
    svm = LinearSVC(); 
    #svm = SVC();# LinearSVC() #SelectorMixin())
    #skf = LeaveOneOut(len(y)) 
    skf = StratifiedKFold(y, 5)
    #rfecv = RFECV(estimator = svm, step=1, cv=StratifiedKFold(y, 5))
    #rfe = RFE(estimator=svm,  step=10, n_features_to_select=100) # cv=StratifiedKFold(y, 5))
    #rfe.fit(X, y)
    #sc = rfe.score(X, y)
    #return sc
    #rfecv.fit(X, y)

    #svm.fit(X, y)
    #print svm.coeff_
    
    pqr = SelectKBest(score_func=chi2, k=k_val)
    pqr.fit(X, y)
    numfeat = len(feats[0])
    mask = pqr.get_support()
    feats2 = []
    for feat in feats:
        feat1 = [feat[i] for i in range(numfeat) if mask[i]]
        feats2.append(feat1)
    X_r = X #numpy.array(feats2)
    
    score = sklearn.cross_validation.cross_val_score(svm, X_r, y, cv=skf, n_jobs=8)
    #X_r = SelectorMixin().transform(X)
    #acc = reduce(lambda x, y: x + y, score)
    #print acc
    avg = reduce(lambda x, y:x + y, score)/float(score.size)
    return avg
    #print score
    #print "Average: " + str(avg)
    #redu
    #print "hello"

kval = 30
#if len(sys.argv) > 1:
#    kval = int(sys.argv[1])

for i in range(kval):
    acc = dostuff(i+1)
    print str(acc) + " : " + str(i+1)
