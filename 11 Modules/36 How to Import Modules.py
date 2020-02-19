# here we will talk about importing modeules in our current file, there are many ways to import modules and there
# members.
# Here we will use devMath.py as module, which has 4 functions or methods and two variables as members


# 1) Basic way
# ----------------------------------------------------------------------------------------------------------------------
import devMath

addition = devMath.d_add(5, 6)
print(addition)

multi = devMath.d_mul(devMath.d_var, 10)  # here d_var = 55
print(multi)
print("-----------")

# 2) Import module as another easy name or short name
# ----------------------------------------------------------------------------------------------------------------------
import devMath as DM

addition = DM.d_add(5, 6)
print(addition)

division = DM.d_div(DM.d_var, 5)
print(division)
print("-----------")

# 3) Directly importing methods/members from module
# ----------------------------------------------------------------------------------------------------------------------
from devMath import d_sub, anyConstantLikePi  # here we don't need to use devMath.d_sub we can directly use it.

subtraction = d_sub(100, 20)
print(subtraction)
print(anyConstantLikePi)
print("-----------")

# 4) import all members from the module
# ----------------------------------------------------------------------------------------------------------------------
from devMath import *  # using this line we can directly access all members present in module devMath

add = d_add(5, 6)
sub = d_sub(50, 10)
mul = d_mul(5, 6)
div = d_div(60, 6)

print("add = ", add, ",sub = ", sub, ",mul = ", mul, ",div = ", div)
print(d_var, ",", anyConstantLikePi)
print("-----------")

# 5) importing members with another/simple name
# ----------------------------------------------------------------------------------------------------------
from devMath import d_add as a, d_sub as s, d_mul as m, d_div as d, d_var as v, anyConstantLikePi as pi

add = a(50, 60)
sub = s(90, 60)
mil = m(50, 60)
div = d(550, 50)

print("add = ", add, ",sub = ", sub, ",mul = ", mul, ",div = ", div)
print(v, ",", pi)
