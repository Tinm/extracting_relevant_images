"""
Student: Adriana Carolina Camacho
Class: Data Mining 
Spring 2016
Python program that makes some corrections to the json file by adding commas after each object
"""
import string
import os.path
import json
import sys
import time 

jsonFile = "restaurantCaptions.txt"
fromP = os.path.dirname(os.path.abspath(__file__)) + "\\"

#read in the json file
lines = []
with open(fromP+jsonFile, encoding="utf8") as f:
    lines = f.readlines()

#add comas between json objects
for i in range(len(lines)):
	if lines[i].find('} {') != -1:	
		lines[i] = lines[i].replace('} {', '},{')

		
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
	
writeFile(lines, fromP, 'newCaptions.json')