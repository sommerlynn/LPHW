def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a+b

def subtract(a, b):
    print "SUBTRACING %d - %d" %(a, b)
    return a-b

def multiply(a, b):
    print "MULTIPLY %d * %d" %(a, b)
    return a*b

def divide(a, b):
    print "DIVIDING %d / %f" %(a, b)
    return a/b


print "CALCUTATING..."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 0.5)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# PAZZLE
print "add(age, subtract(height, multiply(weight, divide(iq, 2))))"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"
