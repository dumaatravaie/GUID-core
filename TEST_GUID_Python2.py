#!/usr/bin/python
# Test possibilty of Duplication of GUID for first 10 characters of hash
# Dipankar Bachar 
# Written in 25/7/2019
# Runs with Python 2
"""This scripts produces more then 1million unique combination of name,surname,dateofbirth,sex from
the file name.csv which is a tsv file and produces GUID for each combination, and checks whether there is
any repetation of GUID ( That is Duplicate GUID ) """
"""Written in python 2.7 
Users can add, or remove more test data in the name.csv file and run this script to check the possibility of duplication of GUID 
For running the program:
Keep the file name.csv and this python script in the same folder and run with python 2.7 from command line """
import hashlib
import sys
import os.path
import re
import unicodedata
# Function to remove special characters and convert them in lower case from typical french names 
def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
# Function to remove special characters from typical french names 
def text_to_id(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return text

container_final={}
C1=[]
C2=[]
C3=[]
C4=[]
C5=[]
C6=[]
# reads the csv file in tsv format and stores each columns in a separate list
infile="./name.csv"
inf=open(infile,"r")
for l in inf:
	k=l.strip().split()
	C1.append(k[0])
	C2.append(k[1])
	C3.append(k[2])
	C4.append(k[3])
	C5.append(k[4])
	C6.append(k[5])
inf.close()

# Produces the combination from the 6 columns data ( 6 lists ) to use as a input for hash alogorithm SHA

for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i])+text_to_id(C2[j])+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
				
# More combination
for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i]+"abcd")+text_to_id(C2[j]+"bc")+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
# More combination
for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i]+"cd")+text_to_id(C2[j]+"ef")+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
				
# More combination
for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i]+"gh")+text_to_id(C2[j]+"ij")+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
# More combination				
for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i]+"kl")+text_to_id(C2[j]+"mn")+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
# More combination
for i in range(0,len(C1)):
	if C1[i]!="NULL":
		for j in range(0,len(C2)):
			new_string=text_to_id(C1[i]+"op")+text_to_id(C2[j]+"qr")+C3[j]+C4[j]+C5[j]+C6[j].lower()
			if not container_final.has_key(new_string):
				container_final[new_string]=1
				

print "Total Number of Combination = "+str(len(container_final))
print "------------------------------------------------- \n "
newGUIDlist={}


# Produces hash and takes the first 10 characters and checks for the Duplicates
for key,value in container_final.items():
	k=hashlib.sha256(key).hexdigest()
	pk=k[0:10]
	print pk
	if not newGUIDlist.has_key(pk):
		newGUIDlist[pk]=1
	else:
		#If duplicate is found print the message and exit the program
		print "BINGO: A Duplicate GUID has been found "
		print "Exiting the Program "
		exit()

# No Duplicate found
print "\n Program terminated normally \n"
print "Total Number of Combination Tested for Duplicate GUID hash = "+str(len(container_final))
print "------------------------------------------------- \n "

print " No duplicate GUID found in "+str(len(container_final))+" combination \n"
	
	
	
	
	