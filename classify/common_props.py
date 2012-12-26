NUM_FOLDS = 10
def getStrFlattened(feats):
   ret = ""
   for feat in feats:
       ret = ret + "_" + str(feat)
   return ret
   
