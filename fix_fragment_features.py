import glob
from math import log
import os

dirname = "fragments"
docFreqMap = {} #Frag Index -> Count of blogposts
fragmentMap = {} #Fragment -> Integer index

featureMap = {}  #Filename -> [(fragIndex, value)]

featIndex = 1
for filepath in glob.glob(dirname + "/*.frag"):
    filename = os.path.basename(filepath)
    featureMap[filename] = []
    
    fragConsidered = {}
    for line in open(filepath):
        
        (frag, count) = line.strip().rsplit("\t")
        
        if frag not in fragmentMap:
            fragmentMap[frag] = featIndex
            featIndex = featIndex + 1
        
        fragHash = fragmentMap[frag]
        featureMap[filename].append((fragHash, count))

        if fragHash not in docFreqMap:
            docFreqMap[fragHash] = 1
        
        if frag not in fragConsidered:
            fragConsidered[frag] = True

            docFreqMap[fragHash] = docFreqMap[fragHash] + 1
            

#print "nothing"

def getLabel(filename):
    if filename.find(".1") != -1:
        return 1
    elif filename.find(".2") != -1:
        return 2
    elif filename.find(".3") != -1 or filename.find(".4") != -1:
        return 3
    assert(False)

'''hello'''    
numDoc = len(featureMap)
for filename in featureMap:
    label = getLabel(filename)
    features = sorted(featureMap[filename])
    
    print label,
    for (feature, value) in features:
        normalizedValue = float(value) * log( float(numDoc)/(float(docFreqMap[feature]) + 1))
        print "  " + str(feature) + ":" + str(normalizedValue),
    print ""

