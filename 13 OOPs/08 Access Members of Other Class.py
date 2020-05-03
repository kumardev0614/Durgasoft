# Here we will see, How to access members of one class inside another class.
# We will create a class Employee with 1 static variable and 3 instance variables.
# NOTE: we cannot access instance variables using ClassName. Instance variables are associated with objects only.
# Then we will create another class Test to access and modify data of Class Employee.
# We will access data by 2 ways: 1) by passing Employee's Object.  2) by passing Employee class itself.
# 1st approach is recommended.


class Employee:
    staticVar = 15

    def __init__(self, enum, ename, esal):
        self.enum = enum
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee number is =', self.enum)
        print('Employee name is =', self.ename)
        print('Employee salary is =', self.esal)


class Test:
    def modifyUsingClassName(emp):
        emp.staticVar = emp.staticVar + 10000
        print('staticVar =', emp.staticVar)

    def modifyUsingClassObject(empObj):
        empObj.esal = empObj.esal + 22000
        empObj.display()


E_Obj = Employee(12, 'dev', 50000)

Test.modifyUsingClassName(Employee)
print('--------------------------')
Test.modifyUsingClassObject(E_Obj)
