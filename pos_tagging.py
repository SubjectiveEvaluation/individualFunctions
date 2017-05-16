import nltk 
text=nltk.word_tokenize("We are going out.Just you and me.")
j,i = 1, 0
a = nltk.pos_tag(text)
for i in range(len(a)):
	print a[i][j]
	