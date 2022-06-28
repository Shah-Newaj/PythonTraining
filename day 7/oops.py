##### Example 1 ##########
# class Myclass:
#     def display(self):
#         print("newaj")
#
# mc=Myclass()
# mc.display()

######### Example 2 ##########
# class Myclass:
#     def m1(self):
#         print("this is instance method")
#
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
#
# m3=Myclass()
# # m3.m2(10,20)
# Myclass.m2(100,200)  #calling the staticmethod using class not through object

### Example 3 ########

# i,j = 15,25         #Global Variables
# class MyClass:
#     a,b = 10,20     #Class Variables
#     def add(self,x,y):      #Local Variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
#
# mc=MyClass()
# mc.add(100,200)

### Example 4 ########

# a,b = 15,25         #Global Variables
# class MyClass:
#     a,b = 10,20     #Class Variables
#     def add(self,x,y):      #Local Variables
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
#
# mc=MyClass()
# mc.add(100,200)

#### Example 5 ############

class MyClass:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("hello...")

MyClass()
mc=MyClass()
mc.m1()