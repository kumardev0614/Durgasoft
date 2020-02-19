# In this file we will see how we can find all members of current/imported module
# we will use python's inbuilt function dir(module_name), it will return a list of all members of the given module


# 1) dir() without any argument
x = 10
y = 50

def f1():
    pass

print(dir())


# ----------------------------------------------------------------------------------------------------------------------
# 2) dir(module_name) with an argument
# comment the 1) code block
p = 15
q = 16

def f1(): pass
def f2(): pass

import devMath
print(dir(devMath))