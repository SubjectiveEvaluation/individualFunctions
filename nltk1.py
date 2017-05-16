from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = 'This is a sample sentence, showing off the stop words filtration. Chehak has very very big sad silly and a wet tkc.Computer software, or simply software, is that part of a computer system that consists of encoded information or computer instructions, in contrast to the physical hardware from which the system is built.'

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example)

#filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

print word_tokens
print filtered_sentence

