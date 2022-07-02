# writing data into text file
# file=open("F:\SQA\SDET\Python Programming for Selenium (2022 New Series)\myfile.txt",'w')
# file.write("This is the first Line.....\n")
# file.write("This is the second Line....\n")
# file.write("This is the third Line....\n")
# file.close()
# print("Program Completed")

# Reading data from file
# file=open("F:\SQA\SDET\Python Programming for Selenium (2022 New Series)\myfile.txt",'r')
# print(file.read())
# file.close()
# print("Reading Completed")

# appending data into text file
file=open("F:\SQA\SDET\Python Programming for Selenium (2022 New Series)\myfile.txt",'a')
file.write("this is the fourth line.....\n")
file.write("this is the fifth line.....\n")
file.close()
print("Appending Completed")