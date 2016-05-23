# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# *arg is pointless, we can just:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# take 1 argument
def print_one(arg1):
    print "arg1: %r" % arg1

# takes no arguments
def print_none():
    print "I got nothing."

print_two("root","shaw")
print_two_again("finch","reese")
print_one("First!")
print_none()
