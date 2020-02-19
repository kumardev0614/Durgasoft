# In this program we will see how we can reload a module explicitly
# Observe this example

# Ex

import module1
import module1
import module1
import module1

print("This is Current file 36 Reloading a module.py")

# By above Example we can see, we have written import statement 4 times but module1 is imported only once
# this is good to not reload same module again and again for performance.
# but sometimes our requirement is to reload same module again and again
# to do so we have a method reload(module_name) which is the member of module "importlib"


# ----------------------------------------------------------------------------------------------------------------------
# Ex----- suppose we are printing data from a module and that data changes in every 30 seconds, to show those changes
# we have to load same module again and again
# for testing purpose we have to change the data manually, we will use sleep() method from time module,
# which will pause the program for 30 sec so that we can change the data manually

# BEFORE RUNNING THIS EXAMPLE COMMENT THE FIRST EXAMPLE

print("program started")
from time import sleep
from importlib import reload
import module1

print()
print("program entered in sleep state")
sleep(20)  # we have to change data of module1 manually in these 30 seconds
reload(module1)  # here we will see the changed data of same module
print()
print("program entered in sleep state again")
sleep(20)
reload(module1)
print("program ended")

# This is not possible normally, because by default module1 will be loaded only once and we cannot see our changes.
