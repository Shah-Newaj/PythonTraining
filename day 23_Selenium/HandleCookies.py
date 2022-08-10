from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies()
print("Size of Cookies: ",len(cookies)) #3

#print details of all cookies
# for c in cookies:
#     # print(c)
#     print(c.get('name'),":",c.get('value'))

#Add new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "12345"})
cookies = driver.get_cookies()
print("Size of Cookies after adding new one: ",len(cookies)) #4

#Delete cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Size of Cookies after deleting one: ",len(cookies)) #3

# Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of Cookies after deleting all cookies: ",len(cookies)) #0


driver.quit()