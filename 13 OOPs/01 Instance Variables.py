# Here we will see 3 ways to declare instance variables
# 1) inside __init__
# 2) inside instance method
# 3) outside the class


class SoftEngg:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name                        # instance variable inside constructor
        self.sal = sal

    def CalcInsentive(self, TargetAchived):
        if TargetAchived is True:
            self.insentive = 5000               # instance variable inside instance method, by self
        else:
            self.sal = self.sal - 1000
            self.insentive = 0


# Raju is not in Target Scheme. So we will not calculate incentive for him
e1 = SoftEngg(1501, 'Raju', 20000)
print(e1.__dict__)

# But Dev is in Target Scheme
e2 = SoftEngg(1502, 'Dev', 20000)
e2.CalcInsentive(True)
print(e2.__dict__)

# Here only raju is disabled, he cannot listen from his left ear, so we cannot add disablity attribute for all
# employees so out side the class we will create a attribute which is only for raju not for other employees

e3 = SoftEngg(1503, 'Ram', 20000)
e3.CalcInsentive(True)
e3.disability = 'Partial deafness'          # instance variable outside the class, by reference variable( of object)
print(e3.__dict__)

e4 = SoftEngg(1504, 'john', 20000)
e4.CalcInsentive(False)
print(e4.__dict__)


# How to delete non required instance variable
# del self.variable_name
# del object_reference.variable_name

del e4.insentive
print(e4.__dict__)


