from sys import argv    # clain that this script will read argv from command line

script, filename = argv # give arguments name

txt = open(filename)    #filename from command line, then return the value of it to txt

print "Here's your file %r:" %filename
print txt.read()        #output the value of txt

print "Type the filename again:"
file_again = raw_input("> ")    #input filename again

txt_again = open(file_again)    #then read the value

print txt_again.read()          #and print it
