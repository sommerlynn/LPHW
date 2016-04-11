x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# position 4

print x
print y

print "i said: %r." % x             # position 3
print "i also said: '%s'." % y      # position 2

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"    # position 1

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
