# Here we will see the use of special variable __name__, it holds the value of source of the current running code
# for Ex--- if we run module2 directly __name__ = __main__ because, current running code's source is __main__ of module2
# but when we import module2 in this file __name__ = module2 because current running file is __name__.py but running
# code is in module2

import module2

x = 99
module2.findCodeSource(x)

def findCodeSource():
    print("this code block is from module", __name__)
    print("x =", x)

findCodeSource()