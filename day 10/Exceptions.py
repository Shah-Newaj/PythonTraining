try:
    num1,num2=10,0
    result=num1/num2
    print("result is", result)
except:
    print("exception handled")
else:
    print("no exceptions occurred")
finally:
    print("always execute")