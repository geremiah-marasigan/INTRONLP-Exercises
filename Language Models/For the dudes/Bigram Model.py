from collections import Counter
import re
import os

print("Loading corpus...")
re_pattern = r'\b[a-zA-Z0-9\-\'\*]+\b|[\.\?\!]'
directory = [
	"Joji's BALLAD Song Lyrics",
#	"Duturte's Speeches",
#	"DLSU Student Publications",
#	"Journal Articles"
]

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
print(total_vocabulary)

dict = {}
test = 0 #Should be equal to 1

for vi in total_vocabulary:
    dict[vi] = term_counter[vi]/total_tokens
    test += dict[vi]

print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
print(dict)
print("This should be equal to 1 (or be close enough): " + str(test))