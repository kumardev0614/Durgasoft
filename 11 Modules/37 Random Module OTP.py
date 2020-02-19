from random import *
from math import *

# In this File we will see use of random module to generate otp of 6 digits.


# 1) from random() method
print('-------random')
for i in range(5):
    print(floor(random() * 1000000))  # but this method has a problem when we have a number 0.02568476913
    # then we will get a 5 digit number, which is not desired


# ----------------------------------------------------------------------------------------------------------------------
# 2) from uniform()
print('--------uniform')
for i in range(5):
    print(floor(uniform(1, 9) * 100000))  # It is a good method, but it does'nt generate otp starting with 0
    # Here the main problem is int data type. If we get an otp like 025698. It will be used as 25698.
    # so we have to use str data type to include 0.


# ----------------------------------------------------------------------------------------------------------------------
# 2.1) from randint()
print('--------randint')
for i in range(10):
    print(randint(100000, 999999))  # But this method has same problem of 2nd method. Always non-zero in staring.


# ----------------------------------------------------------------------------------------------------------------------
# 3) using randint(a,b)
print('------randint and str()')
for i in range(10):
    otp = ''
    for j in range(6):
        otp = otp + str(randint(0, 9))
    print(otp)


# ----------------------------------------------------------------------------------------------------------------------
# 4) alphanumeric otp with alphabet at 1,3,5 position and digit at 2,4,6 position A9L8P2
print('-------alphanumeric')
for i in range(10):
    otp = ''
    for j in range(3):
        otp = otp + chr(randint(65, 90)) + str(randint(0, 9))
    print(otp)


# ----------------------------------------------------------------------------------------------------------------------
# 4.1) alphanumeric using only randint and single for loop
print('--------alphanumeric single loop and randint')
for i in range(10):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep='')
