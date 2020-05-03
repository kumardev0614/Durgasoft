# In functional programming we can use global variable anywhere in program.
# That means it can also be used inside class.

x = 100             # Global variable

class Test:
    def m1(self):
        print(x)    # accessing global variable inside class

    def m2(self):
        print(x)


t = Test()
t.m1()
t.m2()
print(x)            # accessing global variable inside program
print('-----------------')

# OK no problem till here
# Case 2) But what iff we have class variable with same name

k = 555

class A:
    k = 999
    def a1(self):
        print(k)        # We have not used className or self so it will call the global variable
        print(self.k)   # now it will call static variable, using self

    def a2(self):
        print(k)
        print(A.k)      # now it will call static variable, using ClassName


a = A()
a.a1()
a.a2()
print('-------------------')

# Ok that is also easy to understand
# Case 3) now we have local variable with same name

p = 9856
class B:
    p = 626
    def b1(self):
        p = 5555
        print(p)            # Here local variable will have high priority than Global variable
        print(self.p)       # Not need to consider, we are calling class variable


b = B()
b.b1()
print(p)
print('-------------------')

# Now this is the most important case to observe
# Case 4) declaring global variable inside class, can we do that??


class C:
    global s
    s = 77777

    def c1(self):
        global r
        r = 11111
        print(r)
        print(s)

    def c2(self):
        print(r)
        print(s)


c = C()
c.c1()
c.c2()
print(r)
print(s)

# Yes, we can define global variables in class, but it is not recommended approach, because global variable is
# concept of functional programming not OOPs.
