# Here we will learn Pickling and Unpickling
# Pickling -- writing object's values in a file
# Unpickling -- reading the object values from file


import pickle   # This module will be use for pickling and unpickling


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('Employee id = ',self.eno,'Salary: ',self.esal,'Name: ',self.ename,'Address: ',self.eaddr)
        print()


#                                                       # Opening a file emp.dat in write mode as myFile, if
with open("emp0.dat", "wb") as myFile:                   # file is not there python will create emp.dat by itself
    empObj = Employee(15, 'rakesh', 30000, 'Noida')     # creating Employee Object
    pickle.dump(empObj, myFile)                         # writing data in file by dump(object, file) method
    print('pickling of object is completed!!!')

with open("emp0.dat", "rb") as myFile:                   # opening file in read mode as myFile
    obj2 = pickle.load(myFile)                          # loading data of emp.dat in obj2
    obj2.display()

print(type(obj2))
