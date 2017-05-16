from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
print lmtzr.lemmatize('cars')
lmtzr.lemmatize('feet')
lmtzr.lemmatize('people')
lmtzr.lemmatize('fantasized','v')

