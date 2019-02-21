from collections import Counter
import re
import os

f = open('confusionMatrix.txt')
temp = f.read().split("\n")
confMatrix = {}
for words in temp:
        word = words.split("\t")
        confMatrix[word[0]] = word[1]
print(confMatrix)
