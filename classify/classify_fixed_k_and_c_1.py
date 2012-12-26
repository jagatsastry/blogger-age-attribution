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
        feat1 = [float(feat[selectFeat]) for selectFeat in selectFeats]
        feats2.append(feat1)

   # print selectFeats
    classifyAndPrintReports(feats2, None)
    #printFreq(feats2)
    
def classifyAndPrintReports(feats2, score_function):
    X_r = X #numpy.array(feats2)
    #clf = LinearSVC(C=C_value) #tree.DecisionTreeClassifier("gini", min_samples_leaf=10)
    cvalstart = 0.1
    cvals = []
    while cvalstart < 1:
        cvals.append(cvalstart)
        cvalstart = cvalstart + 0.2
    parameters = {'C':cvals}
    svr = LinearSVC()
    clf = grid_search.GridSearchCV(svr, parameters,  refit=True)
    clf.fit(X_r, y)

#   clf = LinearSVC(C=C_value)

    skf = StratifiedKFold(y, 5)
    #avg = reduce(lambda x, y:x + y, score)/float(score.size)
    #print avg
    #tot = reduce(lambda x, y:x + y, score) #print score[0]
    #print tot
    print "****ACCURACIES****"
    accuracies = sklearn.cross_validation.cross_val_score(clf, X_r, y, cv=skf, n_jobs=8 )
    print accuracies

    print clf.best_params_
    print svr.coef_
    '''
    print " Average: " + str(accuracies.mean()) 
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
        prodMap[int(index) - 1] = rule
    return prodMap

def computeFreq(feats2):
    for i in range(3):
        freq.append([0] * len(feats2[0]))

    tot = len(feats2)
    i = 0
    for li  in range(len(feats2)):
        feats1d = feats2[li]
        for fj in range(len(feats1d)):

            freq[labels[li]][fj] = freq[labels[li]][fj] + feats1d[fj]


def printFreq(feats2):
    computeFreq(feats2)
    prodMap = getProdMap(sys.argv[2])
    for i in range(len(selectFeats)):
        if i == 1:
            print [feat[i] for feat in feats2]
        prod = prodMap[selectFeats[i]]
        print "%30s, %5.3f, %5.3f, %5.3f" % (prod, freq[0][i], freq[1][i], freq[2][i])


kval = 345
C_value = 0.08

#for kval in range(500):
acc = dostuff(kval)
