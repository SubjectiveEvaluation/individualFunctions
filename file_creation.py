fr = open('sample.txt','w')

fr.write('This is the first line in the file created\n')
fr.write('This is the last line that end up the file\n')
fr.close()


fr = open('sample.txt','r')

print fr.read()