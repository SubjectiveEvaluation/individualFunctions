from nltk.corpus import wordnet

#syns = wordnet.synsets("good")
synonyms = []
antonyms = []

for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print (set(synonyms))
print "\n"
print (set(antonyms))

print synonyms[2]
