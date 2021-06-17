'''
	About
	=====
	- check if string contains a-z1-5
'''
import re
word = '1bhieosindia148'
pattern = re.compile("[a-z0-5]+")

if pattern.fullmatch(word) != None:
	print("found")
else:
	print("not found")
