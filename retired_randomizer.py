import random
from random import randint
import string

dataSet = []

for i in range (10000):
     addSet = random.randint(0,100)
     dataSet.append(addSet)
     
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    addLetters = random.choice(alphabet)
    dataSet.append(addLetters)
   
poppedSet = [] #Declared outside because I need it following the segAlpha function       
   
def segregateAlpha(dataSet):
    soupAlphabet = []
    for i in dataSet:
        if dataSet.isNumeric(i) == False:
            soupAlphabet.append(i)
            poppedSet = dataSet.pop(i)
    soupAlphabet.sort()
    return soupAlphabet
print(segregateAlpha(dataSet))   

def sortList(dataSet):
    evenList = []
    oddList = []
    for i in dataSet:
        if i % 2 == 0: ##if remainder = 0, put in even
            evenList.append(i)
        else:
            oddList.append(i)
    evenList.sort(), oddList.sort()
    return evenList, oddList        
print(sortList(dataSet))






#def sortList(dataSet):
#    evenList = []
#    oddList = []
#    alphabetSet = []
#    for i in dataSet:
#        if str.isdigit(i):
#            if i % 2 == 0:
#                evenList.append(i)
#            else:
#                oddList.append(i)
#        else:
#            alphabetSet.append(i)            
#    evenList.sort(), oddList.sort(), alphabetSet.sort()
#    return evenList, oddList, alphabetSet        
#print(sortList(dataSet))    