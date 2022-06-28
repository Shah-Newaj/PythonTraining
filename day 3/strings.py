
####### Example concatenate/multiply #########
# s="python"
# print(s+"coding")   #pythoncoding
# print(3*"coding")   #codingcodingcoding

####### Example slicing [] #########
# Starting index starts from 0
# Ending index starts from 1

# s="welcome"
# print(s[1:3])   #el
# print(s[1:])    #elcome
# print(s[:5])   #welco
#
# print(s[1:-1])   #elcom - remove last character
# print(s[:-2])   #welco - remove last 2 characters

####### Example ascii ord() chr() #########

# print(ord("A")) #65
# print(chr(65)) #A

####### Example min() max() len() #########

# print(max('abzdfgc'))   #depending on ascii value
# print(min('abc'))
#
# print(len("abcasdf"))

####### Example in, not in #########

# s='welcome'
# print('come' in s)
# print('come' not in s)

####### Example stirng comparison #########

# print('hello' == 'hello')
# print("hellow" <= "hello")

####### Example stirng testing #########

# s="welcome to Python"
# print(s.isalnum())  #False
# print("Welcome".isalpha())
# print(s.isdigit())  #False

####### Example searching for substring #########

# s="welcome to python"
# print(s.endswith("on")) #True
# print(s.find("me")) #5
# print(s.find("you")) # -1 means not found
# print(s.count("o")) #3

####### Example converting string #########

# s = "welcome to Python"
# s1 = s.capitalize()
# print(s.capitalize())   #Welcome to python
# print(s1)   #Welcome to python
# print("wELCOME".capitalize())   #Welcome
#
# print(s.upper())   #WELCOME TO PYTHON
# print(s.lower())   #welcome to python
# print(s.swapcase())   #WELCOME TO pYTHON
# print(s.replace("to", "in"))   #welcome in Python

####### Example converting string #########
#Method 1
# s="welcome"
# rev_s=""
# for i in s:
#     rev_s=i+rev_s
#     print(rev_s)
# print(rev_s)    #emoclew

#Method 2
# s="welcome"
# rev_s=s[::-1]
# print(rev_s)    #emoclew

