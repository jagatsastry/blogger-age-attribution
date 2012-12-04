import glob
from math import log
import os
import os.path
import sys

import sklearn.svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import numpy
import sklearn.cross_validation
from sklearn.feature_selection.selector_mixin import SelectorMixin
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.cross_validation import LeaveOneOut
from sklearn.feature_selection import RFECV


dirname = "fragments"
docFreqMap = {} #Frag Index -> Count of blogposts
fragmentMap = {} #Fragment -> Integer index

featureMap = {}  #Filename -> [(fragIndex, value)]

featIndex = 1

#files = glob.glob(dirname + "/*.male*frag") # + glob.glob(dirname + "/*.male*frag") 
files = glob.glob(dirname + "/*.2*frag") + glob.glob(dirname + "/*.3*.frag") + glob.glob(dirname + "/*.4*.frag")
#files = glob.glob(dirname + "/*female.1*frag") + glob.glob(dirname + "/*female.2*frag") + \
#        glob.glob(dirname + "/*female.3*frag") + glob.glob(dirname + "/*female.4*.frag")
for i in range(len(files)):
    filepath = files[i]
    sequencedFilename = str(i+100) + "__" +  os.path.basename(filepath)
    featureMap[sequencedFilename] = {}
    
    fragConsidered = {}

    for line in open(filepath):
        
        (frag, count) = line.strip().rsplit("\t")
        
        if frag not in fragmentMap:
            fragmentMap[frag] = featIndex
            featIndex = featIndex + 1
        
        fragHash = fragmentMap[frag]
        featureMap[sequencedFilename][fragHash] = count

        if fragHash not in docFreqMap:
            docFreqMap[fragHash] = 1
        
        if frag not in fragConsidered:
            fragConsidered[frag] = True

            docFreqMap[fragHash] = docFreqMap[fragHash] + 1
            
#print "nothing"

def getLabel(filename):
    if filename.find(".1") != -1:
#        if filename.find(".female") != -1:
#            return 1
        return 2
    elif filename.find(".2") != -1:
#        if filename.find(".female") != -1:
#            return 3
        return 4
    elif filename.find(".3") != -1 or filename.find(".4") != -1:
#        if filename.find(".female") != -1:
#            return 5
        return 6
    #assert(False)

numFeat = featIndex - 1
numDoc = len(featureMap)
labels = []
allFeatures = []
for filename in sorted(featureMap):
    label = getLabel(filename)
    labels.append(label)
    featuresMap1 = featureMap[filename]
    features = []
    for i in range(numFeat):
        norm = 0
        if i+1 in featuresMap1:
            value = featuresMap1[i+1]
            norm = float(value) * log( float(numDoc)/(float(docFreqMap[i + 1]) + 1))
        features.append(norm)
    allFeatures.append(features)


X = numpy.array(allFeatures)
y = numpy.array(labels)
svm = LinearSVC();
#skf = LeaveOneOut(len(y))
skf = StratifiedKFold(y, 10)
#skf = StratifiedShuffleSplit(y, 1000)

csvFile = open(sys.argv[1], "w") #"fragfeats_female.csv", "w")
for i in range(len(labels)):
    csvFile.write(str(labels[i]))
    feats = allFeatures[i]
    for feat in feats:
        csvFile.write("," + str(feat))
    csvFile.write("\n")

score = sklearn.cross_validation.cross_val_score(svm, X, y, cv=skf, n_jobs=8)
avg = reduce(lambda x, y:x + y, score)/float(score.size)
print score
print avg


#x = len(allFeatures)

#        print "  " + str(feature) + ":" + str(normalizedValue),
#    print ""


#print featureMap

#if __name__ == "__main__": print
