class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('Employee id = ',self.eno,'\nSalary: ',self.esal,'\nName: ',self.ename,'\nAddress: ',self.eaddr)
        print()