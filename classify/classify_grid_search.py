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
from sklearn import tree
from sklearn import grid_search
#from sklearn.metrics import *
#from sklearn.metrics import *
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
import sys

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
    
    #rfecv = RFECV(estimator = svm, step=1, cv=StratifiedKFold(y, 5))

freq = []
selectFeats = []
def dostuff(k_val):
    
    selectFeats = []
    pqr = SelectKBest(score_func=chi2, k=k_val)
    pqr.fit(X, y)
    numfeat = len(feats[0])
    mask = pqr.get_support()
    feats2 = []
    indx=0
    for i in range(numfeat):
        if mask[i]:
            selectFeats.append(i)

    for feat in feats:
        feat1 = [int(feat[selectFeat]) for selectFeat in selectFeats]
        feats2.append(feat1)
    #print "%d %d %d" % (k_val, len(feats2[0]),  len(selectFeats))

    classifyAndPrintReports(feats2, None)
    #printFreq()
    
def classifyAndPrintReports(feats2, score_function):
    X_r = numpy.array(feats2)
    #clf = LinearSVC(C=C_value) #tree.DecisionTreeClassifier("gini", min_samples_leaf=10)
    cvalstart = 0.02
    cvals = []
    while cvalstart < 2:
        cvals.append(cvalstart)
        cvalstart = cvalstart + 0.02

    parameters = {'C':cvals}
    svr = LinearSVC()
    clf = grid_search.GridSearchCV(svr, parameters,  refit=True)
    clf.fit(X_r, y)
#    return
#    clf.fit(X_r, y)
#    print "Best score: %0.3f" % clf.best_score
#    print "Best parameters set:"
#    best_parameters = clf.best_estimator.get_params()
#    for param_name in sorted(parameters.keys()):
#        print "\t%s: %r" % (param_name, best_parameters[param_name])

    skf = StratifiedKFold(y, 5)
    #avg = reduce(lambda x, y:x + y, score)/float(score.size)
    #print avg
    #tot = reduce(lambda x, y:x + y, score) #print score[0]
    #print tot
#    print "****ACCURACIES****"
    accuracies = sklearn.cross_validation.cross_val_score(clf, X_r, y, cv=skf, n_jobs=8 )
    #print clf.best_estimator_
    #print clf.grid_scores_
    #print clf.best_estimator_
    #print clf.best_score_
    print clf.best_params_ 
    #print clf.best_estimator_
#    print accuracies 
    print "K: " + str(len(feats2[0])) + ", Average: " + str(accuracies.mean()) 
    '''
    print
    print "***PRECISION RECALL, FSCORE AND SUPPORT***"
    pr_recall_fscore = sklearn.cross_validation.cross_val_score(clf, X_r, y, cv=skf, n_jobs=8, score_func=precision_recall_fscore_support)
    print pr_recall_fscore
    print "Average: \n" + str(reduce(lambda x, y:x + y, pr_recall_fscore)/float(len(pr_recall_fscore)))
    print ""
    print "***CONFUSION MATRIX***"
    cmatrix_score = sklearn.cross_validation.cross_val_score(clf, X_r, y, cv=skf, n_jobs=8, score_func=confusion_matrix)
    print cmatrix_score
    print
    print "Total: \n" + str(reduce(lambda x, y:x + y, cmatrix_score))
    '''
    '''
    class_report = sklearn.cross_validation.cross_val_score(clf, X_r, y, cv=skf, n_jobs=8, score_func=classification_report)
    print "****CLASSIFICATION REPORT********"
    print "Number %d" % len(class_report)
    for x in class_report:
        print x
        '''
        


def getProdMap(mapfile):
    prodMap = {}
    for line in open(mapfile):
        temp = line.split("###")
        (rule, index) = (temp[0], temp[1])
        prodMap[int(index)] = rule
    return prodMap

def computeFreq(feats2):
    for i in range(3):
        freq.append([0] * len(feats2[0]))

    tot = len(feats2)
    for feats1d in feats2:
        for i in range(len(feats1d)):
            freq[labels[i]][i] = freq[labels[i]][i] + feats1d[i]


def printFreq(feats2):
    computeFreq(feats2)
    prodMap = getProdMap(sys.argv[2])
    for i in range(len(selectFeats)):
        prod = prodMap[selectFeats[i]]
        print "%30s%5d%5d%5d" % (prod, freq[0][i], freq[1][i], freq[2][i])


kval = 360
C_value = 0.1

i=1
while i < 500:
   acc = dostuff(i)
   i=i+1
