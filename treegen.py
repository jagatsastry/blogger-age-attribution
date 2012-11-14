#Note: Pass the blogposts dir as the argument
from post_reader import readPosts
from nltk.tree import Tree
from corenlp_client import StanfordNLP
import os
import sys
import shutil
from random import randint

#shutil.move("b", "b")
#exit(0)
nlp = StanfordNLP()

def getTrees(post):
    result = nlp.parse(post)
    trees = []
    for sent in result['sentences']:
        trees.append(sent['parsetree'])
    return trees

blog_dir = sys.argv[1] #"blogs/sample_blogs"
treebanks_dir = "treebanks"
postsmap = readPosts(blog_dir, 0)


MAX_POSTS = 1

for key in postsmap:
    if len(postsmap[key]) == 0: continue
    print "Generating trees for " + key
    postnum = randint(0, len(postsmap[key]) - 1)
    post = postsmap[key][postnum]
    numwords = len(post.split())
    if(numwords < 100 or numwords > 600): continue
#    for post in postsmap[key]:
    treebankFile = treebanks_dir + "/" +  key + "_" + str(postnum) + ".tb"

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
    print "Trees generated for " + key
    print "Moving it to all_processed_blogs"
    shutil.move(blog_dir + "/" + key, "all_processed_blogs")

