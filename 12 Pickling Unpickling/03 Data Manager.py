# Give your all inputs here and store them is file emp.dat

import empData, pickle

f = open('emp.dat','wb')
n = int(input('enter number of employees: '))

for i in range(n):
    eno = int(input("enter id of Employee: "))
    ename = input('enter name: ')
    esal = int(input('enter salary: '))
    eaddr = input('enter address: ')
    e = empData.Employee(eno, ename, esal, eaddr)
    pickle.dump(e,f)
    print(i+1, 'record submitted')
