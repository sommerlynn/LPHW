from sys import argv

script, filename = argv

print """We're going to ERASE %r.
If you don't want that, hit CTRL -C (^C).
If you do want that, hit RETURN.""" %filename

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# print "Truncating the file. Goodbye"
#target.truncate()

print "Now input thre lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Writing these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "Close it."
target.close()
