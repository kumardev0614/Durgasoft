# Here we will see how static method works.

class devMath:

    @staticmethod
    def d_add(a, b):
        return a + b

    @staticmethod
    def d_mul(a, b):
        return a * b

    @staticmethod
    def d_div(a, b):
        return a/b

print(devMath.d_add(10,50))
print(devMath.d_mul(10,50))
print(devMath.d_div(10,50))


# Now we will see how to identify static method
# Case 1)
class test:

    def m1():
        print('some method')

t = test()
# t.m1()

# Here PVM will treat it as instance method, but there is no self variable to point towards current onject.

# Case 2)
class B:

    def m1():   # ignore this red underline
        print('some method 2')

B.m1()
# No problem we can call static methods by class name.
# If we will try to call using object reference it will became case 1.

# Case 3)
class C:
    @staticmethod
    def m1():
        print('some method 3')

c = C()
c.m1()
# what??? How???
# Yes we can call static methods by object reference but there should be @staticmethod decorator.

# Case 4)
class D:
    def m1(x):
        print("value of x is:", x)

d = D()
#d.m1(10)    it will generate error

# Why???
# Here we are passing value 10 in x and then printing it, what can the problem
# First, Cause we are calling the method using object reference, it will be treated as instance mathod.
# second, actually we are passing 2 arguments here first is value for self, second is int 10
# but in definition we have only one argument, that is the problem.

# Case 5)
class E:
    def m1(x):
        print("again value of x is:", x)

E.m1(20)

# Now we are calling the method with class name, it will considered as static method. No Errors.






