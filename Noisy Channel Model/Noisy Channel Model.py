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

for word in unigram:
    unigram[word] /= vocabulary_count

"----- Methods -----"

def getP(word):
    return unigram.get(word,word)

def correction(word): 
    return max(candidates(word), key=getP)

def candidates(word): 
    return (known([word]) or known(edits(word)) or [word])

def known(words):
    return set(w for w in words if w in unigram)

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
    print(str(newWord) + ": ("+str(unigram[newWord])+")")
