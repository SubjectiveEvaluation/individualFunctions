from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example = ["python",'pythonr','phthoning','pythoned','pythonoly']

for w in example:
	print ps.stem(w)

sentence = 'This is a sample sentence, showing off the stop words filtration. Chehak has very very big sad silly and a wet tkc.Computer software, or simply software, is that part of a computer system that consists of encoded information or computer instructions, in contrast to the physical hardware from which the system is built.'
words = word_tokenize(sentence)

for w in words :
	print ps.stem(w)

