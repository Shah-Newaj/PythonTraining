from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
noOfColumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

print(noOfRows) #7
print(noOfColumns) #4

driver.close()
