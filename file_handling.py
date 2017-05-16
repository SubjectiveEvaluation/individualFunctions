def handling_file():
	with open('sample.txt') as f:
		content = f.readline()
		while content:
		 	print content
	 		content = f.readline()
	f.close()
handling_file()