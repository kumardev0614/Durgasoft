# Here in this file we will see many important and mostly used methods of random Module
from random import *
from math import *


# 1) random()
print('---------random()---------------')
# it will generate float values between 0 and 1, not including 0 and 1, 0<x<1
for x in range(5):
    print(random())


# ----------------------------------------------------------------------------------------------------------------------
# 2) randint(a,b)
print('---------randint()---------------')
# it will generate INT values between a and b, including a,b
# a<= x <=b
for x in range(10):
    print(randint(1, 16))


# ----------------------------------------------------------------------------------------------------------------------
# 3) uniform(a,b)
print('---------uniform()---------------')
# it will generate FLOAT values between a and b, not including a,b
# a<x<b
for x in range(20):
    print(uniform(1, 10))


# ----------------------------------------------------------------------------------------------------------------------
# 4) randrange(start, end, step)
print('---------randrange()---------------')
# it generates random values from a given range
# start<= x < end      it includes start value but excludes end value
# default values of start = 0, and step = 1,   means randrange(10) <==> randrange(0,10,1)

# for x in range(10):
#     l1.append(randrange(10))

l1 = [randrange(10) for x in range(10)]
print(l1)

l2 = [randrange(1, 11) for x in range(10)]
print(l2)

l3 = [randrange(1, 11, 2) for x in range(10)]
print(l3)
# difference between randint(a,b) and randrange(a,b,s) is that randint does'nt have step argument


# ----------------------------------------------------------------------------------------------------------------------
# 5) choice(sequence/collection)
print('---------choice()---------------')
# it returns a random object from a given collection, but that collection should support indexing

print(choice([10, 60, 88, 22, 55]))  # from list
print(choice((10, 60, 88, 22, 55)))  # from tuple
# print(choice({10,60,88,22,55})) not possible, set does not support indexing

for x in range(10):
    print(choice('devendra'))  # from string
