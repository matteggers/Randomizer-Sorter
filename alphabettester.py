import random
from random import randint
import string

dataSet = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    addLetters = random.choice(alphabet)
    dataSet.append(addLetters)
    
print(dataSet)