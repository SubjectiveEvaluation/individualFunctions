from nltk.corpus import wordnet
similar=[]
for ss in wordnet.synsets('small'):
    #print(ss)
    	for sim in ss.similar_tos():
        	print('    {}'.format(sim))
