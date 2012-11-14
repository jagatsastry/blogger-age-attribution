import os
import glob
from random import sample
from random import shuffle


def readPosts(dirname, index):
    postmap = {}
    print "Reading all posts from " + dirname
    allPosts = sample(glob.glob(dirname + "/*female*xml"), 50) + sample(glob.glob(dirname + "/*.male*xml"), 50)
    shuffle(allPosts)
    for filepath in allPosts:
        #filename = "3776017.female.17.Student.Libra.xml"
        #filepath = dirname + "/" + filename

        posts = getPostsFromFile(filepath)
        postmap[os.path.basename(filepath)] = posts
#        postmap[index] = postmap[index] + posts
    return postmap


def getPostsFromFile(filepath):
    posts = []
    xmlfile = open(filepath)
    #print "Handling " + filepath
    filestring = xmlfile.read()
    temparr = filestring.split("<post>")[1:]
    for temp in temparr:
        posts.append(temp.split("</post>")[0].strip())
    
    return posts
        
if __name__ == '__main__': print readPosts("blogs/sample_blogs", 0)
#readPosts("blogs/sample_blogs", 0)
#readPosts("blogs/20s", 1)
#readPosts("blogs/3040s", 2)
#TEST_POST = "In Memoriam.  father's day 2001  the last day i saw Richie Lynch.We spent the evening at the poolside where his sister Gina worked at the time.. my sisters were there and a few other good friends and we all had a blast. Richie and i even went on one of the East End's famous 7-11 runs.. he was the Notorious 'Salt Daddy' to my sister Patrice,and he got her some Fritos. and he would get the shitty nachos for my sister Colleen, filling the top part of the nacho holder with a ton of the nasty hot cheese-food product. We had the best talk about life and the universe, about how we all would spend the holidays together, all our families, kids, siblings.. we had such happy thoughts and dreams. we were singing along to the radio and we saw a hot pursuit police chase through the tiny crap ass town of Southold.we went back to the house and we stayed out very late, all of us at Gina's, talking, enjoying and laughing. Richie had the knack to make everyone feel good about being around him, and helped everyone to feel better about themselves. I remember that night, Patrice was self-concious about her bikini and he kept saying she looked like a goddess, how beautiful she was and how he felt she was so gorgeous, inside and out. He was telling me what a good woman i was, and how he respected me and was happy for me in my life. he was spending good time with Colleen, who had loved him deeply for so long, and who was just so happy being in his company. His sister Gina was a caretaker at a home for mentally challenged adults, and we were hanging out with the guys in the house that night. One loved Richie like a brother and follwed him around all the time. Richie would treat him equally, as we all did, but they way he treated him was just so touching, it made me cry. He was a loving, caring, man who shared his heart and soul with so many people and touched so many lives.   July 29, 2001.  I was in my car in the parking lot of the Merriweather Post Pavilion, with my friends Jen and Stacey, about to go into my 15th and last BNL show of that summer.We were awaiting the arrival of my brother Billy, who was going to the show and i was so happy and excited. Stacey's cell phone rang suddenly and it was my mom. She sounded sad and colmly told me to sit and said' A terrible thing happened. my heart stopped. I knew someone had died. Richie Lynch was killed in a car accident this morning i dropped the phone and screamed. screamed No. over and over again.my friends were trying to comfort me and i got the phone back. my mom just told me to stay where i was and that my brother would stop there to see me and then he'd be coming up. I knew i could not just leave my car in Maryland. i know i could not drive yet. i knew that i had school the next day. so i stayed there. my brother came by and hugged me and we cried. Some girls gave me a beer and hugged me. i never saw them again. i went into the show, i had found my friend Fred and we watched Action Figure Party and he  just held me quietly as we sat in the rain.we went to our seats and listened to Vertical Horizon. BNL came out and i actually cried through the whole concert. i cried and cried. i looked up at the sky and sobbed and asked over and over again 'why?'.after the show i fell apart more and my friend Dana drove my car and Fred drove me to his apartment in NJ. the next day i went home and the mourning began.when i went into the car to drive home, the radio turned on and the song that was playing hit me so hard..the lyrics fit perfectly and i KNEW Richie was there with me. i knew we had a new angel in our lives watching over us. And i have felt him with me every single day since.  I miss you Richie. Thank you for the time we had. Thanks for loving my family and being like a brother. you are always an angel in my heart.  the song that was playing was the same song Richie and I sang together on the way back from 7-11 the last night i saw him..  (words by james taylor) .  Just yesterday morning they let me know you were gone  Susanne the plans they made put an end to you I walked out this morning and I wrote down this song  I just can't remember who to send it to I've seen fire and I've seen rain I've seen sunny days that I thought would never end  I've seen lonely times when I could not find a friend  But I always thought that I'd see you again  Won't you look down upon me, Jesus  You've got to help me make a stand  You've just got to see me through another day  My body's aching and my time is at hand  And I won't make it any other way Oh, I've seen fire and I've seen rain I've seen sunny days that I thought would never end I've seen lonely times when I could not find a friend But I always thought that I'd see you again  Been walking my mind to an easy time  my back turned towards the sun  Lord knows when the cold wind blows it'll turn your head around  Well, there's hours of time on the telephone line  to talk about things to come Sweet dreams and flying machines in pieces on the ground  Oh, I've seen fire and I've seen rain I've seen sunny days that I thought would never end I've seen lonely times when I could not find a friend  But I always thought that I'd see you, baby, one more time again, now  Current Mood: melancholy Current Music: 'Soma' - Smashing Pumpkins."
