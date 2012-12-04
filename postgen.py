#Note: Pass the blogposts dir as the argument
from post_reader import readPosts
from nltk.tree import Tree
from corenlp_client import StanfordNLP
import os
import sys
import shutil
from random import randint
import glob

#shutil.move("b", "b")
#exit(0)
nlp = StanfordNLP()

def getTrees(post):
    result = nlp.parse(post)
    trees = []
    for sent in result['sentences']:
        trees.append(sent['parsetree'])
    return trees

blog_dir = "all_processed_blogs"
treebanks_dir = "treebanks_final"
postsmap = readPosts(blog_dir, 0)

for blog in glob.glob(treebanks_dir + "/*.xml*tb"):
    (key, postnumstr) = os.path.basename(blog).split(".tb")[0].split("_")
    postnum = int(postnumstr)
#    (filename, postnum) = key.split("_")
    print "Obtaining blog num " + str(postnum) + " from " + key
    post = postsmap[os.path.basename(key)][postnum]
    postFileName = "300_posts/" + key + "_" + str(postnum) + ".post";
    if  os.path.exists(postFileName):
        continue
    postFile = open(postFileName, "w")

    postFile.write(post)

