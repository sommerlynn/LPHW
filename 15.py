from sys import argv
# clain that this script will read argv from command line
script, filename = argv
# give arguments name
txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
