import os
treebanks_dir = "treebanks"
blog_dir = "blogs/sample_blogs"
postnum=10000
treebank = open(treebanks_dir + "/" + os.path.basename(blog_dir) + "." + str(postnum) + ".tb", "w")

