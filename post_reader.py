from xml.dom.minidom import parse

import os

def readPosts(dirname, index):
    postmap = [[], [], [], []]
    for filename in os.listdir(dirname):
        #filename = "3776017.female.17.Student.Libra.xml"
        filepath = dirname + "/" + filename

        posts = getPostsFromFile(filepath)
        postmap[index] = postmap[index] + posts
    return postmap


def getPostsFromFile(filepath):
    posts = []
    xmlfile = open(filepath)
    print "Handling " + filepath
    filestring = xmlfile.read()
    temparr = filestring.split("<post>")[1:]
    for temp in temparr:
        posts.append(temp.split("</post>")[0].strip())
    
    return posts
        
if __name__ == '__main__': print readPosts("blogs/sample_blogs", 0)
#readPosts("blogs/sample_blogs", 0)
#readPosts("blogs/20s", 1)
#readPosts("blogs/3040s", 2)
