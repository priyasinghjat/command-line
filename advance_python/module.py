# first method to call a module 
import module1
print(module1.sum(10,20))
print(module1.mult(12,24))

# second method to call a specific function then use this method

from module1 import sum
print(sum(34,45))

# to import whole module then use this

from module1 import *
print(sum(39,89))
print(mult(24,34))

# to make alias of the function

import module1 as m
print(m.sum(89,90))