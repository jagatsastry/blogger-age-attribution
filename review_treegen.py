#Note: Pass the blogposts dir as the argument
from post_reader import readPosts
from nltk.tree import Tree
from corenlp_client import StanfordNLP
import os
import sys
import shutil
from random import randint

nlp = StanfordNLP()

def getTrees(post):
    result = nlp.parse(post)
    trees = []
    for sent in result['sentences']:
        trees.append(sent['parsetree'])
    return trees

rev_file = sys.argv[1] 


treebanks_dir = "treebanks"
postnum = 0
for post in open(rev_file): 
    treebankFile = treebanks_dir + "/" +  os.path.basename(rev_file) + "_" + str(postnum) + ".tb"

#        if postnum  + 1 > MAX_POSTS:
#            break
    print "   Post# " + str(postnum)
    postnum = postnum + 1
    if  os.path.exists(treebankFile):
        continue

#        print post
    allTrees = getTrees(post)
    treebank = open(treebankFile, "w")
    for tree in allTrees:
        treebank.write(str(tree) + "\n")
    treebank.close()
    #print "Moving it to all_processed_blogs"
    #shutil.move(blog_dir + "/" + key, "all_processed_blogs")

