# retrieve your data here by giving no of Employees in range(n)

import pickle

f = open('emp.dat','rb')
print('Employee Details....\n')
for i in range(3):
    obj = pickle.load(f)
    obj.display()

