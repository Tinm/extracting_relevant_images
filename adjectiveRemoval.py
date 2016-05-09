import string
"""
Student: Adriana Carolina Camacho
Class: Data Mining 
Spring 2016
Python program that uses a text file to make a list of adjectives to remove from 
a json formated file 
"""
import os.path
import sys 
import time 

adjFile = "adjectiveList.txt"
freqFile = "frequency_words.txt"
fromP = os.path.dirname(os.path.abspath(__file__)) + "\\"

#read in the adjwords from file 
adjwords = [line.rstrip('\n') for line in open(fromP+adjFile)]
print(adjwords)
print(len(adjwords))

#read in the freq file
lines = []
with open(fromP+freqFile, encoding="utf8") as f:
    lines = f.readlines()
	
#REMOVE adjective WORDS
for i in range(100): 
#for i in range(len(lines)):
	print (i)
	#print(lines[5])
	#print (lines[i])
	for j in adjwords:
		adj = j + ','
		if adj in lines[i]:
			print('adj: ' + adj)
			print(lines[i])
			del lines[i]
			break

		
#write to a file from a list of contents 97 chars at a time
# pck 	= list of packages
# path2 = path where file will be stored
# file 	= name of the file
def writeFile(pck, path2, file):			
	print ('number of packages: %d' % len(pck))
	newPath = path2 + file
	print (newPath)

	if os.path.isfile(newPath): #if the file already exists
		st = str(time.time())	#timestamp
		n = file[:file.find('.')] #get the name of the original file
		t = file[file.find('.'):] #get the type (ie .txt, .csv, etc)
		newPath = path2 + n + '(' + st + ')' + t #attach timestamp to filename
	file = open(newPath, 'w', encoding='utf-8')
	file.writelines(["%s" % item for item in pck])
	file.close
	
writeFile(lines, fromP, 'newFreq.txt')