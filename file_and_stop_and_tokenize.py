from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv
import sqlite3


con=sqlite3.connect("project.db")
cur= con.cursor()
	
with open('sample.txt') as f:
	content = f.readline()
	#print content
	while content:
		#print content
		stop_words = set(stopwords.words('english'))
		word_tokens = word_tokenize(content)
	
		filtered_sentence = []
		
		for w in word_tokens:
			if w not in stop_words:
				cur.execute("CREATE TABLE sample_ans(Words TEXT,answer_number INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,question_number INT DEFAULT 1, POS VARCHAR(50) NOT NULL,freq INTDEFAULT 1, similar TEXT NULL );")
				cur.execute('INSERT INTO sample_ans VALUES(w,NULL,1,'pos',,'hi')')

				con.commit()
		cur.execute('SELECT * FROM sample_ans')	
				#new_f = open('sample1.txt','a')
				#new_f.write(w)
				#new_f.write('\n')
				#new_f.seek(1,1)
				#wr = csv.writer(new_f,delimiter=';')
				#wr.writerows(w)
				#wr.writerows(w)
				#filtered_sentence.append(w)
				
#		print word_tokens
#		print filtered_sentence

	#	content = f.readline()

new_f.close()
#l = len(filtered_sentence)
#writer=csv.writer(open('sample1.csv','wb'))
#i = 0	
#while i != l:
#	writer.writecolumn(filtered_sentence[i])
#	i = i+1



con.close()



