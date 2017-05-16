import nltk
#from nltk.corpus import stopwords 			
from nltk.tokenize import word_tokenize 
import collections
import sqlite3

con = sqlite3.connect('table.db') #connection to connect to database
cur = con.cursor() #variable to execute statements 
cur.execute('DROP TABLE IF EXISTS OriginalAnswers;') #Re-creates the existing table ! (I guess)
cur.execute('CREATE TABLE OriginalAnswers(Words TEXT , Q_Num INT , Ans_Num INT UNSIGNED , POS TEXT DEFAULT NULL, Freq INT ,Similar TEXT);') #creates table with given coloumns
i,x,count = 1,0,1
with open('answers.txt') as f:	#opens the file in ''
	content = f.readline()		#reading the first line of the text file
	while content:	#reads every line in the file 
		#stop_words = set(stopwords.words("english")) #setting stop_words set as ENGLISH LANGUAGE.
		words = word_tokenize(content)	#tokenizing the words in the example
		
		filtered_sentence = []
		a = nltk.pos_tag(words) #part of speech of each word
		x = 0
		for w in words:
			if w in filtered_sentence:
				count += 1 #for increasing the frequency of the repetitive words
			filtered_sentence.append(w)	#tokenized stop word free list

			cur.execute('INSERT INTO OriginalAnswers(Words , Q_Num , Ans_Num , POS , Freq , Similar) VALUES (?,?,?,?,?,?);',(w,1,i,a[x][1],count,"synonym"))
			x +=1	#incrementing the pos list
			count = 1 #incrementation for the repetitive words
			con.commit()				
		#print filtered_sentence		#printing a list without stop words		
		i += 1	
		count = 1
		content = f.readline() #increments to next line in text file
#cur.execute('create table TempTable as select distinct * from OriginalAnswers;')

#cur.execute('truncate table OriginalAnswers;')

#cur.execute('insert into OriginalAnswers select * from TempTable;')


DELETE FROM Words
 WHERE id NOT IN (SELECT * 
                    FROM (SELECT MAX(n.Freq)
                            FROM Words n
                        GROUP BY n.Words) x)

cur.execute("SELECT * FROM OriginalAnswers;")
data = cur.fetchall()
con.close()
