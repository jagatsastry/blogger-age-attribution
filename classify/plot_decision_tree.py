import sklearn.svm
from common_props import *
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import numpy
import sklearn.cross_validation
from sklearn.feature_selection.selector_mixin import SelectorMixin
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.cross_validation import LeaveOneOut
from sklearn.feature_selection import RFECV
from sklearn import tree
import StringIO, pydot 

#Task specific python code
from  feats_edgebn import *

FEAT_STR = getStrFlattened(RFE_FEATS)

def getAccuracies(depth):
    
    feats = []
    labels = []
    fem = 0
    male = 0
    for line in open(CSV_FILE): #open("sex01.csv"):
        line = line.strip(" \n")
        arr = line.split(",") 
	sex = int(float(arr[0]))
        labels.append(int(float(arr[0])))
        #feature = [ float(x) for x in arr ]
        feature = [ float(arr[x+1]) for x in RFE_FEATS ]
        feats.append(feature)
#	for feat in feature:
#		if feat > 0.44 and sex >= 1:
#			fem = fem + 1
#		elif feat > 0.44 and sex < 1:
#			male = male + 1
#    print "Fem: " + str(fem) + " male: " + str(male)     	
    
    
    y = numpy.array(labels)
    X = numpy.array(feats)
    
    clf = tree.DecisionTreeClassifier("gini", min_samples_leaf=10); 
    #clf = LinearSVC()
    #skf = LeaveOneOut(len(y)) 
    #skf = StratifiedShuffleSplit(y, 1000)

    #skf = StratifiedKFold(y, 10)
    #score = sklearn.cross_validation.cross_val_score(clf, X, y, cv=skf, n_jobs=8)
    clf.fit(X, y)
    dot_data = StringIO.StringIO() 
    tree.export_graphviz(clf, out_file=dot_data) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_png("pngs/" + CSV_FILE + "_graph_" + FEAT_STR + ".png") 

    return 0 #score

for depth0 in range(1):
	score = getAccuracies(depth0 + 1)
