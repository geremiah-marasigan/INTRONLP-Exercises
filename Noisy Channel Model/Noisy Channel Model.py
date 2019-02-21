from collections import Counter
import re
import os

re_pattern = r'\b[a-zA-Z0-9\-\'\*]+\b|[\.\?\!]'
directory = [
	"Joji's BALLAD Song Lyrics",
	"Duturte's Speeches",
	"DLSU Student Publications",
	"Journal Articles"
]

all_tokens = []
text_files = []
term_counter = Counter()
total_tokens = 0
for folder in directory:
	file_names = os.listdir(folder)

	for file_name in file_names[:]:
		with open(folder + "/" + file_name, 'r', encoding='utf8') as f:
			title = file_name[:-4]
			temp = {
				"Title": title,
				"Raw Text": f.read()
			}
			temp['Tokens'] = re.findall(re_pattern, temp["Raw Text"].lower())
			temp['Vocabulary'] = list(set(re.findall(re_pattern, temp["Raw Text"].lower())))
			
			print("===%s===" % title)
			print("Total tokens: %s" % len(temp['Tokens']))
			print("Total vocabulary: %s" % len(temp['Vocabulary']))
                        
			total_tokens += len(temp['Tokens'])
			all_tokens += temp['Tokens']
			text_files.append(temp)
			term_counter.update(temp['Tokens'])

print("---Identifying vocabulary...---")
# Find vocabulary set
total_vocabulary = set()
for song in text_files:
	total_vocabulary |= set(song['Vocabulary'])
total_vocabulary = list(total_vocabulary)
vocabulary_count = len(total_vocabulary)
print("Vocabulary count: %s" % vocabulary_count)
print("Grand Total Tokens in Corpus: %s" % total_tokens)

unigram = {}
for token in all_tokens:
    unigram[token] = unigram.get(token,0) + 1

f = open('confusionMatrix.txt')
temp = f.read().split("\n")
confMatrix = {}
for words in temp:
        word = words.split("\t")
        confMatrix[word[0]] = word[1]

"----- Methods -----"
#finds the edit needed between the given word and the candidate word through minimum edit distance 
def editMade(word1,word2):
        #edit is nothing
        if(word1 == word2):
                return ""
        #edit is transpose
        elif(len(word1) == len(word2) and sorted(word1) == sorted(word2)):
                diff = [i for i in range(len(word1)) if word1[i] != word2[i]]
                return str(word1[diff[0]]) + str(word1[diff[1]]) + "|" + str(word2[diff[0]]) + str(word2[diff[1]])
        #edit is replacing
        elif (len(word1) == len(word2)):
                diff = [i for i in range(len(word1)) if word1[i] != word2[i]]
                return str(word1[diff[0]]) + "|" + str(word2[diff[0]])
        #edit is insert
        else:
                str1len = len(word1)
                str2len = len(word2)

                array = [[0 for x in range(str2len+1)] for y in range(str1len+1)]

                for x in range(str1len+1):
                        array[x][0] = x

                for x in range(str2len+1):
                        array[0][x] = x

                num1 = 0
                num2 = 0
                num3 = 0

                #Creating table
                for x in range(1,str1len+1):
                        for y in range(1,str2len+1):
                                if(word1[x-1] == word2[y-1]):
                                        num1 = array[x-1][y-1]
                                else:
                                        num1 = array[x-1][y-1] + 2 #S
                                        num2 = array[x][y-1]+1 #I
                                        num3 = array[x-1][y]+0 #D

                                if (num1 <= num2) and (num1 <= num3):
                                        array[x][y] = num1
                                elif (num2 <= num1) and (num2 <= num3):
                                        array[x][y] = num2
                                else:
                                        array[x][y] = num3      

                                x = str1len
                                y = str2len
                                path = []

                                #Back-Trace
                                while(x > 0 or y > 0):
                                        if(word1[x-1] == word2[y-1]):
                                                num1 = array[x-1][y-1]
                                        else:
                                                num1 = array[x-1][y-1] + 2
                                        num2 = array[x][y-1]+1
                                        num3 = array[x-1][y]+0

                                        if (num1 <= num2) and (num1 <= num3):
                                                if(num1 > array[x-1][y-1]):
                                                        path.append('S')
                                                else:
                                                        path.append('M')
                                                        x-=1
                                                        y-=1
                                        elif (num2 <= num1) and (num2 <= num3):
                                                path.append('I')
                                                y-=1
                                        else:
                                                path.append('D')
                                                x-=1
                                if(len(word1) < len(word2)):
                                        for x in range(len(path)):
                                                if(path[x] == 'I'):
                                                    return str(word1[len(word1)-1-x]) + "|" + str(word1[len(word1)-1-x]) + str(word2[x-1])
                                else:
                                        for x in range(len(path)):
                                                if(path[x] == 'D'):
                                                        return str(word1[len(word1)-1-x]) + str(word2[x-1]) + "|" + str(word1[len(word1)-1-x])

#gets the count of the edit from the confusion matrix and divides it by the number of times the candidate word appears in the corpus
def getPxWord(word1,word2):
        return float(confMatrix.get(editMade(word1,word2),0))/ unigram[word2]

#gets the count of a word in corpus and divides it by the total number of unique words in corpus
def getP(word):
        return unigram[word]/vocabulary_count

#given a word returns the most likely word or the word itself if not an error or not in corpus
def correction(word):
        correctWords = candidates(word)
        print(correctWords)
        if((word in correctWords and len(correctWords) == 1) or word in unigram):
                return [str(word),str(1)]
        PxWordPWord = {}
        for newWord in correctWords:
                PxWordPWord[newWord] = getPxWord(word,newWord) * getP(newWord)
        print(PxWordPWord)
        maxNum = 0
        bestWord = ""
        for key in PxWordPWord:
                if(PxWordPWord[key] > maxNum):
                        maxNum = PxWordPWord[key]
                        bestWord = key
        return [str(bestWord),str(maxNum)]

#gives a list of candidate words based on if the word exists in the corpus or if an edited version of the word exists in the corpus or if the word does not exist in the corpus
def candidates(word): 
        return (known([word]) or known(edits(word)) or [word])

#returns a set of all words that exist in corpus
def known(words):
        return set(w for w in words if w in unigram)

#returns every possible single edit for the provided word
def edits(word):
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

while(True):
        inp = input("Enter a Word: ")
        newWord = correction(inp)
        if(newWord[0] not in unigram):
                print(str(newWord[0]) + ": word not in corpus")
        else:
                print(str(newWord[0]) + ": ("+str(newWord[1])+")")
