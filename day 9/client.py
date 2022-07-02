import sys
sys.path.append("C:/Users/Shah Newaj/PycharmProjects/PythonTraining/day 9/pack1")

#Approach 1 (Better Approach)
import module1
import module2

module1.display()
module2.show()

#Approach 2
from module1 import *
from module2 import *

display()
show()