from collections import Counter
import re
import os


def minimum(str1, str2):
    str1len = len(str1)
    str2len = len(str2)

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
            if(str1[x-1] == str2[y-1]):
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

#    print("-------------------------------")
#    print("Distance: " + str(array[str1len][str2len]))
#    print("-------------------------------")
    return array[str1len][str2len]

print("Loading corpus...")
re_pattern = r'\b[a-zA-Z0-9\-\'\*]+\b|[\.\?\!]'
directory = [
	"Joji's BALLAD Song Lyrics",
#	"Duturte's Speeches",
#	"DLSU Student Publications",
#	"Journal Articles"
]

text_files = []
all_tokens = []
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
			all_tokens+=temp['Tokens']
            
			total_tokens += len(temp['Tokens'])
			text_files.append(temp)
			term_counter.update(temp['Tokens'])

print("---Identifying vocabulary...---")
#print(all_tokens)
# Find vocabulary set
total_vocabulary = set()
for song in text_files:
	total_vocabulary |= set(song['Vocabulary'])
total_vocabulary = list(total_vocabulary)
vocabulary_count = len(total_vocabulary)
print("Vocabulary count: %s" % vocabulary_count)
print("Grand Total Tokens in Corpus: %s" % total_tokens)
#print(total_vocabulary)
    
dict = {}
test = 0 #Should be equal to 1

for vi in total_vocabulary:
    dict[vi] = term_counter[vi]/total_tokens
    test += dict[vi]

print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
#print(dict)
print("This should be equal to 1 (or be close enough): " + str(test))
print(all_tokens[len(all_tokens)-1])
bigrams = []
for x in range(len(all_tokens)-1):
    bigrams.append(all_tokens[x] + " " + all_tokens[x+1])

token_count = {}
for token in all_tokens:
    if(token in token_count):
        token_count[token] +=1
    else:
        token_count[token] = 1

bigram_count = {}
for token in bigrams:
    if(token in bigram_count):
        bigram_count[token] +=1
    else:
        bigram_count[token] = 1

bigram_probability = {}
for vocab in total_vocabulary:
    bigram_probability[vocab] = {}
    count = token_count[vocab]
    listofpairs = []
    for token in bigram_count:
        if(token.split(" ")[0] == vocab):
            listofpairs.append(token)
    for pair in listofpairs:
        bigram_probability[vocab][pair.split(" ")[1]] = bigram_count[pair]/count

print(bigram_probability)


