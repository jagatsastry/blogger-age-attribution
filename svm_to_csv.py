import sys

svmfile = sys.argv[1]

maxfeatnum = 0

labels = []
featHashes = []
for line in open(svmfile):
    vals = line.split()
    label = int(vals[0])
    featHashMap = {}
    for temp in vals[1:]:
        (featstr, valstr) = temp.split(":")
        (feat, val) = (int(featstr), float(valstr))
        featHashMap[feat] = val
        if maxfeatnum < feat:
            maxfeatnum = feat
    
    labels.append(label)
    featHashes.append(featHashMap)

features = []
for i in range(len(labels)):
    feature = []
    featHashMap = featHashes[i]
    for i in range(maxfeatnum):
        j = i + 1
        if j in featHashMap:
            feature.append(featHashMap[j])
        else:
            feature.append(0)

    features.append(feature)

for i in range(len(labels)):
    print str(labels[i]),
    for feat in features[i]:
        print "," + str(feat),
    print ""


