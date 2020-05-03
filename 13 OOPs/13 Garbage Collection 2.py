# Note: We have GC module to enable or disable GC.
# But disabling garbage collector varies from platform to platform.
# Means gc.disable() will not work in every OS or IDE

import gc
import sys


print(gc.isenabled())       # To check GC is enable or not, returns True or Fales
gc.disable()                # To disable GC
print(gc.isenabled())
gc.enable()                 # To enable GC
print(gc.isenabled())


print('---------------------------------------------------------------------------------------------------------------')
# Multiple reference and Garbage Collector


class Test:
    def __init__(self):
        print('**********Object is Created**********')

    def __del__(self):
        print('**********Object is destroyed************')


t1 = Test()
t2 = t1
t3 = t2
t4 = t3

del t1
del t2
print('After deleting t1 and t2, object is not available for GC')

del t3
print('Not after t3 also')

del t4
print('Now it is available for GC')
print('End of the Program')


print('---------------------------------------------------------------------------------------------------------------')
# How many references are associated with an object
# getrefcount() method from sys modules is used to count that.
p1 = Test()
p2 = p1
p3 = p2
p4 = p3
print(sys.getrefcount(p1))
# p1,p2,p3,p4,self are 5 references.


print('---------------------------------------------------------------------------------------------------------------')
# if list object is available for GC, means every object present in list is available for GC.

list1 = [Test(), Test(), Test()]
list1 = None
