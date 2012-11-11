import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

if __name__ == "__main__":
    nlp = StanfordNLP()
    result = nlp.parse("Hello world!  It is so beautiful.")
    result = nlp.parse("Hmmmmm... I don't actually know what I am going to post, but I will do it Ad Lib. We made a new song today to the tune of A Pizza Hut. It goes like this: A big fat chicken, A big fat Chicken, a furry little rabbit and a big fat chicken. A big fat chicken, a big fat chicken. A furry little_and_nbsp;rabbit and a big fat chicken. AN AARDARK AN AARDVARK, a furry little rabbit and a big fat chicken. AN AARDVARK AN AARDVARK, a furry little rabbit and a big fat chicken. (repeat as many times as amuses) Oh and me and Josh (yeah I know Josh and I. You're just like my mum.) designed a pencil case with Arthur the Aardvark on it. Well it wasn't the trashy rubbish Arthur the Aardvark off the BBC who looks more like a mouse and the only reason he's_and_nbsp;called an Aardvark is cos Arthur the mouse sounds rubbish. This was the real Arthur the Aardvark. He had a real snout and was gobbling up ants at the rate of 10 to a dozen. hmmmmm...I'm bored. Camp in 2 days. Yay. I don't think anyone actually goes on this site anyway. Huh who cares. YOU ALL SUCK. Well with the exception of a few choice people. (NO GEORGE THAT DOESN'T INCLUDE YOU.) well i'm even more bored than when i started this blog.   Why? Why? Why? Only you hold the answers.")
    pprint(result)

    from nltk.tree import Tree
    tree = Tree.parse(result['sentences'][0]['parsetree'])
    print (result['sentences'][0]['parsetree'])
    #print tree
    #pprint(tree)
