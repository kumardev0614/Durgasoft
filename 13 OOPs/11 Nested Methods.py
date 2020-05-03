# Nested Methods
# We can Make methods inside methods in python, it is not possible in Java.


class Test:
    @staticmethod
    def addAndMul(a, b):

        def Sum(p, q):
            Sum = p + q
            print(Sum)

        def addTen(j):
            j = j + 10
            return j

        Sum(a, b)

        a = addTen(a)
        b = addTen(b)
        Sum(a, b)

        a = addTen(a)
        b = addTen(b)
        Sum(a, b)

        a = addTen(a)
        b = addTen(b)
        Sum(a, b)


t = Test()
t.addAndMul(10,20)