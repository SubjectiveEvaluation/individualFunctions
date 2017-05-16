import nltk
from nltk.corpus import stopwords 			
from nltk.tokenize import word_tokenize 
from collections import Counter
import re
import sqlite3
import math
import string
from itertools import chain
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
from pywsd.utils import lemmatize, porter, lemmatize_sentence, synset_properties

with open('answers.txt') as f:	#opens the file in ''
	content = f.readline()		#reading the first line of the text file
	while content:	#reads every line in the file 
		#print content
		
		stop_words = set(stopwords.words("english")) #setting stop_words set as ENGLISH LANGUAGE.

		words = word_tokenize(content)	#tokenizing the words in the example
		
		filtered_sentence = []
		
		k = dict(Counter(words))
		#print k
		a = nltk.pos_tag(words)
		print a
