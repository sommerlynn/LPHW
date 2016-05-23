def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheese!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print ""

from sys import argv
script, amount_of_cheese, amount_of_crackers = argv
print "use argv from command line:"
cheese_and_crackers(int(amount_of_cheese), int(amount_of_crackers))


print "cheese_and_crackers(20, 30)"
cheese_and_crackers(20, 30)

print "cheese_and_crackers(amount_of_cheese, amount_of_crackers)"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "cheese_and_crackers(10 + 20, 5 + 6)"
cheese_and_crackers(10 + 20, 5 + 6)

print "cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print"raw_input the numbers:"
amount_of_cheese = raw_input("Number of cheese:> ")
amount_of_crackers = raw_input("Number of crackers:> ")
cheese_and_crackers(int(amount_of_cheese), int(amount_of_crackers))
