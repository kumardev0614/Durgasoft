# Here we will see what are static variables, where we can declare them, How to access them
# Static variables are class level variables which are same for all objects of the class. If we change the value of
# one variable by any object, it will be changed for all objects.


class MyClass:
    a = 10                      # 1) Inside class

    def __init__(self):         # 2) Inside __init__, using ClassName
        MyClass.b = 20
        self.c = 30

    def m1(self):               # 3) Inside Instance method, using Classname
        MyClass.d = 40
        self.e = 50

    @classmethod                # 4) Inside Class method, using cls variable or ClassName
    def c_method(cls):          # Here cls does not represents object, it represents class itself.
        cls.f = 60
        MyClass.g = 70

    @staticmethod               # 5) Inside static method, using ClassName
    def s_method(self):         # Static method does not takes object as it's first argument,
        MyClass.h = 80          # self does not represents current object. Here self is treated as normal argument
        print('self =',self)


obj = MyClass()
obj.m1()
obj.c_method()
obj.s_method(525698)
MyClass.i = 90                  # 6) Outside the class, using ClassName

print(obj.__dict__)
print(MyClass.__dict__)


# How to access Static variables
print()
print('How to access Static variables')
print()


class Test:
    a = 15

    def __init__(self):
        print('init by object', self.a)
        print('init by Class', Test.a)

    def m1(self):
        print('m1 by object', self.a)
        print('m1 by Class', Test.a)

    @classmethod
    def c_method(cls):
        print('c_method by cls', cls.a)
        print('c_method by Class', Test.a)

    @staticmethod
    def s_method():
        print('s_method by Class', Test.a)


t = Test()
print('outside by object', t.a)
print('outside by Class', Test.a)
t.m1()
t.c_method()
t.s_method()
print()
Test.c_method()
Test.s_method()
print(t.__dict__)

print('-----------------------------------')
# How we can change value of static variable
# We can change the value of static variable only by using ClassName or cls (if it is a class method)
# If we use object reference or self, it will create a instance variable for that object with same name


class abc:
    a = 10
    b = 15


s1 = abc()                              # Here a = 10,  b = 15
s2 = abc()                              # also a = 10,  b = 15
print(s1.__dict__, s2.__dict__)         # there is no any instance variable
s1.a = 99                               # Now python will create an instance variable a = 99
print('s1.a =', s1.a, 's1.b =', s1.b)   # a = 99(instance variable)  b = 15(static variable)
print('s2.a =', s2.a, 's2.b =', s2.b)   # a = 10(static variable)    b = 15
print(s1.__dict__, s2.__dict__)         # {'a': 99} {}
print()

del s1.a                                # s1.a = 99 is deleted
abc.a = 9658                            # static a = 9658
print('s1.a =', s1.a, 's1.b =', s1.b)   # s1.a = 9658 s1.b = 15
print('s2.a =', s2.a, 's2.b =', s2.b)   # s2.a = 9658 s2.b = 15
print(s1.__dict__, s2.__dict__)

print()