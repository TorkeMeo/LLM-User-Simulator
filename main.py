import math

def initialize():
    index = {}
    return index

def add(index,word):
    index[word]=0

def count(index,sentence):
    totalcount=0
    word=""
    for i in sentence:
        if word !="" and (i==" " or i=="," or i=="."):
            totalcount +=1
            for j in index:
                if word == j:
                    index[j]+=1
            word=""
        elif word =="" and (i==" " or i=="," or i=="." or i=="?" or i=="!"):
            continue
        else:
            word+=i
    return totalcount


def show(index,totalcount):
    totalcount=0
    print("words count:",end="[")
    for w in index:
        print(w,":",index[w],"  ",end="")
    print("]\n")
    print("TF-IDF:",end="[")
    for g in index:
        totalcount +=index[g]
    for x in index:
        if index[x]!=0:
            print(x,":",index[x]/totalcount*math.log(1+totalcount/index[x])," ",end="")
        else:
            print(x, ":", 0, " ", end="")
    print("]\n")
    print("binary weighting:[",end="")
    for x in index:
        if index[x] != 0:
            print(x,":",1," ",end="")
        else:
            print(x, ":", 0, " ", end="")
    print("]\n")




def elementadd(index):
    sign=0
    while sign !=1:
        word=str(input("add key:"))
        add(index,word)
        sign = int(input("input 1 to stop. input 0 to continue:"))

def sentencecount(index):
    signal = 0
    totalcount = 0
    while signal != 1:
        sentence = str(input("input sentence:"))
        totalcount+=count(index,sentence)
        signal = int(input("input 1 to stop. input 0 to continue:"))

data=initialize()
elementadd(data)
num=sentencecount(data)
show(data,num)


