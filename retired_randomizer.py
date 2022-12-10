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
<<<<<<< HEAD:retired_randomizer.py
   
poppedSet = [] #Declared outside because I need it following the segAlpha function       
   
def segregateAlpha(dataSet):
    soupAlphabet = []
=======
    
  
numList = []
soupAlphabet = []
evenList = []
oddList = []
 
def segAll(dataSet):
>>>>>>> db409ea4621f3926e4e7960fbd25d6533d3854df:randomizer.py
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
    evenList.sort(), oddList.sort(), soupAlphabet.sort()
    return soupAlphabet, evenList, oddList
print(segAll(dataSet))

