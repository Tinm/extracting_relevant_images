"""
Student: Adriana Carolina Camacho
Class: Data Mining 
Spring 2016
Python program that uses a text file to make a list of stop words to remove from 
a json formated file 
"""
import string
import os.path
import json
import sys 
import time 

stopFile = "stop.txt"
jsonFile = "0_0_0.txt"
fromP = os.path.dirname(os.path.abspath(__file__)) + "\\"

#read in the stopwords from file 
stopwords = [line.rstrip('\n') for line in open(fromP+stopFile)]
#print(stopwords)

#read in the json file
lines = []
with open(fromP+jsonFile, encoding="utf8") as f:
    lines = f.readlines()

print(len(lines))
#REMOVE STOP WORDS
#for i in range(100): 
for i in range(len(lines)):
	if lines[i].find('  "CAPTION" : ') != -1:
		#print(i)		
		lines[i] = lines[i].upper()
		
		for j in stopwords:
			
			#lines[i] = lines[i].replace(' ' + j.upper()+' ', ' ')
			#lines[i] = lines[i].replace('"' + j.upper()+ ' ', '"')
			#lines[i] = lines[i].replace(' ' +j.upper()+'"', '"')
			#lines[i] = lines[i].replace('(' +j.upper()+' ', '(')
			#lines[i] = lines[i].replace(' ' +j.upper()+')', ')')
			#lines[i] = lines[i].replace('-' +j.upper()+' ', '-')
			#lines[i] = lines[i].replace(' ' +j.upper()+'-', '-')
			#lines[i] = lines[i].replace(j.upper()+',', ' ')
			#lines[i] = lines[i].replace(j.upper()+'!', ' ')
			#lines[i] = lines[i].replace(j.upper()+'.', ' ')
			#lines[i] = lines[i].replace('&', '') 
			lines[i] = lines[i].replace(' ' + j.upper()+'ness ', ' ')
			lines[i] = lines[i].replace('"' + j.upper()+ 'ness ', '"')
			lines[i] = lines[i].replace('"' + j.upper()+ 'ness"', '""')
			lines[i] = lines[i].replace(' ' +j.upper()+'ness"', '"')
			lines[i] = lines[i].replace('(' +j.upper()+'ness ', '(')
			lines[i] = lines[i].replace(' ' +j.upper()+'ness)', ')')
			lines[i] = lines[i].replace('-' +j.upper()+'ness ', '-')
			lines[i] = lines[i].replace(' ' +j.upper()+'ness-', '-')
			lines[i] = lines[i].replace(j.upper()+'ness,', ' ')
			lines[i] = lines[i].replace(j.upper()+'ness!', ' ')
			lines[i] = lines[i].replace(j.upper()+'ness.', ' ')
			
			lines[i] = lines[i].replace(' ' + j.upper()+'s ', ' ')
			lines[i] = lines[i].replace('"' + j.upper()+ 's ', '"')
			lines[i] = lines[i].replace('"' + j.upper()+ 's"', '""')
			lines[i] = lines[i].replace(' ' +j.upper()+'s"', '"')
			lines[i] = lines[i].replace('(' +j.upper()+'s ', '(')
			lines[i] = lines[i].replace(' ' +j.upper()+'s)', ')')
			lines[i] = lines[i].replace('-' +j.upper()+'s ', '-')
			lines[i] = lines[i].replace(' ' +j.upper()+'s-', '-')
			lines[i] = lines[i].replace(j.upper()+'s,', ' ')
			lines[i] = lines[i].replace(j.upper()+'s!', ' ')
			lines[i] = lines[i].replace(j.upper()+'s.', ' ')
		#print (lines[i])

		
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
	
writeFile(lines, fromP, 'noAdjStopPhoto.json')