import pickle

class Employee:
    def __init__(self, a):
        self.a = a
        print("constructor called")

    def display(self):
        print('a = ',self.a)

obj1 = Employee(15)
print(obj1.__dict__)
obj1.__init__(16)
print(obj1.__dict__)

