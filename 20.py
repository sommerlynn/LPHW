from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #point to the start

def print_a_line(line_count, f):
    print line_count,f.readline()

current_file = open(input_file)

print "1. Print the whole file:\n"
print_all(current_file)

print "2. Rewind"
rewind(current_file)

print "3. print 3 lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
