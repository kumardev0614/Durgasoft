# Garbage Collection
import time

# Here destructor __del__() is not responsible for destruction of useless object.
# Garbage collector destroys the useless object, but just before destruction of object it calls __del__()
# to deallocate resources, close Database connection or network connection etc.
# Here in example we will see --
# If we point any object to none, the object is immediately available for GC. We can see __del__ is called
# in running program.
# But if we don't do that my ourselves, then GC will destroy the objects just before ending the program.


class Test:
    def __init__(self):
        self.a = 5
        print(self, 'Object is created, then values are initialized by __init__ ')

    def m1(self):
        print(self.a)

    def __del__(self):
        print(self, 'destructor __del__ called for cleanup, then Object is destroyed')


t = Test()
t.m1()
t2 = Test()

t2.m1()
t = None

time.sleep(5)
print('End of program')