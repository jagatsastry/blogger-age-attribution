Project Title: Blogger Age Attribution Using Syntactic Stylometry


Predicting the age group of a blogger based on the grammatical structure of their blog post.

Age groups: 10s, 20s and 30 and above
Accuracy obtained: 72%

Dependencies: scikit-learn, numpy, core-nlp python wrapper over Stanford PCFG parser, Frequent fragment extractor (disco-dop)

-----------------------------------------------
Abstract from our project report
-----------------------------------------------
In this project, we investigated if bloggers of a particular age range follow a certain syntactical
structure in their blog posts, which can be mined using syntactic stylometric techniques. In contrast
to the earlier work which focused on the lexical features of blogposts, we focused on the latent
grammatical structure that can be discovered in the writing style of bloggers. We experimented with
different syntactic stylometric techniques based on Probabilistic Context Free Grammar (PCFG)
parse trees and obtained good results and some interesting insights in the writing style of bloggers of different age groups. 
We also investigated if the classification gets better when the gender of the blogger is known. 
This, coupled with the analysis of gender classification, gives interesting insights into the effect of gender on the 
way a blogger of a particular age group writes. In addition to analyzing the confusion matrix obtained, 
we experimented with various binary classification schemes, selecting two age groups at a time to see 
if it gives further insights into the similarity of writing styles of authors belonging to different age groups. 
