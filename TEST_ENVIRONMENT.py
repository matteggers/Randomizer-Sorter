import random
from random import randint
import string

dataSet = []

for i in range (1000):
     addSet = random.randint(0,100)
     dataSet.append(addSet)
     
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    addLetters = random.choice(alphabet)
    dataSet.append(addLetters)
      
numList = []
soupAlphabet = []
evenList = []
oddList = []
 
def segAll(dataSet):
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
    evenList.sort(), oddList.sort()
    return soupAlphabet, evenList, oddList
print(segAll(dataSet))

