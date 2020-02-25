import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('eno',self.eno,'esal',self.esal,'ename',self.ename,'eaddr',self.eaddr)


with open("emp.dat", "wb") as myFile:
    empObj = Employee(15, 'rakesh', 30000, 'Noida')
    pickle.dump(empObj, myFile)
    print('pickling of object is completed!!!')

with open("emp.dat", "rb") as myFile:
    obj2 = pickle.load(myFile)
    obj2.display()
