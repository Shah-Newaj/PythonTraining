import sys
sys.path.append("C:/Users/Shah Newaj/PycharmProjects/PythonTraining/day 9/packA")
sys.path.append("C:/Users/Shah Newaj/PycharmProjects/PythonTraining/day 9/packB")

import emp

empobj = emp.Employee(101,"Shah", 50000)
empobj.displayemp()

import stu

stuobj=stu.Student(1,"Newaj",3.75)
stuobj.displaystu()