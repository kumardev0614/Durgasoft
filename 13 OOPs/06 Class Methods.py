# Here we will see why and how to use class methods.


class A:
    a = 15
    b = 16

    def MySum(self):
        return self.a+ self.b

a = A()
print(a.__dict__)
print(a.MySum())

# In above example we are accessing static variables by object. But if there is no instance variable in MySum()
# method why we have to create an instance method.
# Also when calling the MySum() we have to create object of class A, and creating an object is very costly operation
# So to increase the efficiency of the code we should use declare MySum as Class method
print('-'*30)


class B:
    p = 30
    q = 20

    @classmethod
    def MySum(cls):
        return cls.p + cls.q

print(B.MySum())

# In above example we don't need any object to call the MySum() method. Which will increase the performance.
# And this is the recommended approach

# ----------------------------------------------------------------------------------------------------------------------
# When to use class method
# Write a program to count number of objects created in a class.
print('-'*30)


class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def showNoOfObjects(cls):
        print("Number of objects created:", cls.count)

a1 = Test()
a2 = Test()
a3 = Test()
a4 = Test()
a5 = Test()
Test.showNoOfObjects()