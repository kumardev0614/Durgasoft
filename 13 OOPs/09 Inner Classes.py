# What are inner classes: The class which is declared inside another class.
# When to use inner classes?
# Without existing one type of object if there is no chance of existing another type of object then
# we should go for inner class.
# Ex - only Engine object cannot exist without car object.
# Ex2 - Department object of University Object.


class Outer:
    def __init__(self):
        print('Outer object created')

    class Inner:
        def __init__(self):
            print('Inner object created')

        def m1(self):
            print('Inner Method Called')


# Here we cannot make inner objects without creating Outer objects.
# i = Inner()            NameError: name 'Inner' is not defined

o = Outer()
i = o.Inner()
i.m1()

# 2nd way
print('-----------')
i2 = Outer().Inner()
i2.m1()

# 3rd way
print('-----------')
Outer().Inner().m1()

# 4th way
print('-----------')
Outer.Inner().m1()
# ----------------------------------------------------------------------------------------------------------------------


# Now we can say that
# Without Existing OUTER class object there is no chance of existing INNER class object.
# Inner class object is always associated with outer class object.
print('--------------------------------------')
# Now we will see efficient use of inner class.


class Person:
    def __init__(self):
        self.name = "Devendra"
        self.dob = self.DOB()  # inner object creation using outer object, dob(innerObj) = self(OuterObj).DOB()
        # Here dob is inner object which is also a instance variable of outer class
        # Now when dob object type variable will get created it will have its 3 instance variable values 14, 6, 1996

    def display(self):
        print('Name of Person:', self.name)
        self.dob.displayDate()
        print('DOB is', self.dob.dd, self.dob.mm, self.dob.yy)

    class DOB:
        def __init__(self):
            self.dd = 14
            self.mm = 6
            self.yy = 1996

        def displayDate(self):
            print('Date of birth is:{}/{}/{}'.format(self.dd, self.mm, self.yy))


Person1 = Person()
Person1.display()

# Here we are creating inner class for DOB because we need 3 variables dd, mm, yy. One thing we can do is creating
# 3 instance variables dd,mm,yy of person class. But these variables are not the part of Person class.
# Person class don't need 3 instance variables dd mm yy. Because dd mm yy is not the property of a person.
# It is the property of DOB. Also DOB cannot exist without person.

# Another thing we can do is creating dob(int or string) = 14061996 for person class.
# But here we cannot perform operations like sorting by date, sorting by year etc.
