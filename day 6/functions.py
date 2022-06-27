######### Example 1 ##############
# def myfun():
#     print("hello")
#
# myfun()

######### Example 2 ##############
def myfun(name):
    print("hello", name)

myfun("newaj")   #hello newaj

######## Example 3 ###############
def cal(a,b):
    print(a+b)

cal(10,20)

######## Example 4 ###############
def cal(a,b):
    return (a+b)

sum=cal(10,20)
print(sum)
print(cal(10,20))