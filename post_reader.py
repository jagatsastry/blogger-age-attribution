from xml.dom.minidom import parse

import os

def readPosts(dirname, index):
    postmap = [[], [], [], []]
    for filename in os.listdir(dirname):
        #filename = "3776017.female.17.Student.Libra.xml"
        xmlfile = open(dirname + "/" + filename)
        print "Handling " + filename
        data = parse(xmlfile)

        postsDom = data.getElementsByTagName("post")
        posts = [post.firstChild.data for post in postsDom]
        for elem in posts:
            postmap[index].append(elem.strip())
    return postmap
        


#readPosts("blogs/sample_blogs", 0)
#readPosts("blogs/20s", 1)
#readPosts("blogs/3040s", 2)
