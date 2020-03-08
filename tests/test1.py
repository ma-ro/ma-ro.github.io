import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = cwd + '/index.md'
search = str(sys.argv[1])

def check_if_string_in_file(file_name, string_to_search):
	count = 0
	f = open(file_name, 'r')
	Lines = f.readlines() 
	regEx = string_to_search + '([A-Z]|[a-z])+'
	for line in Lines:
		if re.findall(regEx, line):
			print("regex")
		if string_to_search in line:
			return True
		count = count + 1
		if count == 100:
			return False
	f.close()
	
	return False


if check_if_string_in_file(directory, (search + ' ')):
   print('Yes')
else:
   print('No')