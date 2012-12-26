#Generates files required for 5-fold cross validation 
#that can be used for classification using SVM
NUM_FOLDS = 5

zero_feats = []
for line in open("Sex0.csv"):
    vals = line.split(",")

    i = 1
    sex0 = []

    for val in vals:
       sex0.append( (i, val))
       i = i + 1
    
    zero_feats.append(sex0)


one_feats = []
for line in open("Sex1.csv"):
    vals = line.split(",")

    i = 1
    sex0 = []

    for val in vals:
       sex0.append( (i, val))
       i = i + 1
    
    one_feats.append(sex0)


num_feats = len(zero_feats)

TRAIN_PER_FOLD = num_feats/NUM_FOLDS

for foldnum in range(NUM_FOLDS):
    trainfile = open("svmfiles/train_" + str(foldnum), "w")
    testfile = open("svmfiles/test_" + str(foldnum), "w")

    idx = 0
    for line in zero_feats:
        
        if idx / TRAIN_PER_FOLD != foldnum:
	    featfile = trainfile
        else:
            featfile = testfile

        featfile.write("-1")
        for (feat, val) in line:
           featfile.write(" " + str(feat) + ":" + str(val))
        idx = idx + 1


    idx = 0
    for line in one_feats:
         if idx / TRAIN_PER_FOLD != foldnum:
             featfile = trainfile
         else:
             featfile = testfile

         featfile.write("+1")
         for (feat, val) in line:
             featfile.write(" " + str(feat) + ":" + str(val))
         idx = idx + 1

