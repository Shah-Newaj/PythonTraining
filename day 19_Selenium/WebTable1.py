from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Count Number of rows and columns
noOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
noOfColumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

# print(noOfRows) #7
# print(noOfColumns) #4


# 2. Read specific row and column data - Master In Selenium
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# 3. Read all the rows and columns
print("Printing rows and columns: ................")
# for r in range(2,noOfRows+1):
#     for c in range(1,noOfColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='    ')
#
#     print("\n")

# 4. Read data baased on condition () List book name whose authon is Mukesh
for r in range(2,noOfRows+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"    ",authorName,"    ",price)


driver.close()
