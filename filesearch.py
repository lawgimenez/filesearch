import sys

filename = raw_input("What filename are you looking for? ")

if len(sys.argv) < 2:
	print "Please enter a directory to search."
	sys.exit()

directory_to_search = sys.argv[1]

import os

if not os.access(directory_to_search, os.F_OK):
	print "Not a valid directory."
	sys.exit()

print "Searching inside " + directory_to_search

for (path, dirs, files) in os.walk(directory_to_search):
	for the_file in files:
		print "File: " + the_file

		if filename == str(the_file):
			print "File found."
			sys.exit()

print
print "File not found."



