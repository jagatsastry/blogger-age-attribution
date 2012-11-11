from post_reader import readPosts
from nltk.tree import Tree
from corenlp_client import StanfordNLP

nlp = StanfordNLP()

def getTrees(post):
    result = nlp.parse(post)
    trees = []
    for sent in result['sentences']:
        trees.append(sent['parsetree'])
    return trees

postsmap = readPosts("blogs/sample_blogs", 0)
treebank = open("treebank", "w")

for post in postsmap[0]:
    for tree in getTrees(post):
        treebank.write(str(tree) + "\n")

