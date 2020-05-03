# Here we will see why and how we can use Setter and Getter methods


class Student:
    pass


s1 = Student()
s1.name = 'raju'
s1.marks = 345

print("Hi", s1.name)
print("Your marks are:", s1.marks)

# here in above example, we are assigning some data to Student object and then accessing that data.
# But this is the worst way of assigning and accessing the data, because there is no security while doing that.
# This is not wrong but not acceptable.
print('-'*20)

class Student1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_data(self):
        print("Hi", self.name)
        print("Your marks are:", self.marks)

s2 = Student1('raju', 356)
s2.show_data()

# here in above example, this approach is good we are not assigning and accessing data directly
# We can write some validation code in show_data() method before providing the data
# Again approach is right, but not standard
print('-'*20)

class Student2():

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


s3 = Student2()
s3.setName('raju')
s3.setMarks(425)
print("Hi", s3.getName())
print("Your marks are:", s3.getMarks())

# Now this approach is right and standard also.
# We use use setter and getter for every instance variable of the class.
# This provide the security to data while assigning and accessing.
# We can validate the user before assigning and accessing.
# If a user failed in validation he cannot read or write data.
# Hiding data behind methods is called ENCAPSULATION.
