import random
from random import randint
import string

dataSet = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

numList = []
soupAlphabet = []
evenList = []
oddList = []

for i in range (100):
     addSet = random.randint(0,100)
     dataSet.append(addSet)
     
for i in range(100): 
    addLetters = random.choice(alphabet)
    dataSet.append(addLetters)

def segAll(dataSet):
    global numList #global allows you to call variable outside of the function
    global soupAlphabet 
    global evenList 
    global oddList 
    for i in dataSet:
        if isinstance(i, int): #checks to see if i is an integer
            numList.append(i)
        else:
            soupAlphabet.append(i)
            
    for i in numList:
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    evenList.sort(), oddList.sort(), soupAlphabet.sort(), numList.sort()
    return soupAlphabet, evenList, oddList, numList

segAll(dataSet) 

#https://www.w3schools.com/python/python_file_write.asp

#f = open("numList.txt", "x")
#g = open("soupAlphabet.txt", "x")
#h = open("evenList", "x")
#k = open("oddList.txt", "x")
#
#def writer(): #experimental, unsure of status
#    fA = open("numList.txt", "a")
#    f.write(numList)
#    f.close
#
#    gA = open("soupAlphabet.txt", "a")
#    g.write(soupAlphabet)
#    g.close
#
#    hA = open("evenList", "a")
#    h.write(evenList)
#    h.close
#
#    kA = open("oddList.txt", "x")
#    k.write(oddList)
#    k.close()
#
#    return fA, gA, hA, kA


def printer():
    print("This is numList!\n")
    print(numList)
    print("\n")
    print("This is alphabetsoup!\n")
    print(soupAlphabet)
    print("\n")
    print("This is evenList\n")
    print(evenList)
    print("\n")
    print("This is oddList!\n")
    print(oddList)

printer()

#https://www.w3schools.com/python/python_variables_global.asp

