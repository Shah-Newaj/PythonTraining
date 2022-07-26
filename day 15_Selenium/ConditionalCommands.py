from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

# is_displayed()   is_enbaled()
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status: ",searchbox.is_displayed()) #True
print("Display Status: ",searchbox.is_enabled()) #True

# is_selected()
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Default radio button status:")
print("Male Status: ",rd_male.is_selected())
print("Female Status: ",rd_female.is_selected())

print("After Clicking on Male Radio Button:")
rd_male.click() #click on male radio button
print("Male Radio Button Status: ",rd_male.is_selected()) #True
print("Female Radio Button Status: ",rd_female.is_selected()) #False

print("After Clicking on Female Radio Button:")
rd_female.click() #click on female radio button
print("Male Radio Button Status: ",rd_male.is_selected()) #True
print("Female Radio Button Status: ",rd_female.is_selected()) #False

driver.quit()